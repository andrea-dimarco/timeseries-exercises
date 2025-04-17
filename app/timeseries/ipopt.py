from pyoptsparse import OPT, Optimization
import numpy as np
import os



class IPOPT:

    def __init__(self, obj_function, problem_name:str="Optimization Problem", quiet:bool=True):
        self.quiet(quiet=quiet)
        self.init_problem(obj_function=obj_function, problem_name=problem_name)


    def quiet(self, quiet:bool|None=None) -> bool:
        if not (quiet is None):
            self.__quiet = quiet
        return self.__quiet


    def add_var(self, name:str, lower:float|None=None, upper:float|None=None, type:str='c', starting_val:float|None=None) -> None:
        if not (starting_val is None):
            self.__problem.addVar(name,
                                type,
                                lower=lower,
                                upper=upper,
                                value=starting_val,
                                )
        else:
                self.__problem.addVar(name,
                                type,
                                lower=lower,
                                upper=upper,
                                )
    

    def add_var_group(self, name:str, n_vars:int, lower:float|None=None, upper:float|None=None, type:str='c', starting_vals:list[float]|None=None) -> None:
        if not (starting_vals is None):
            assert len(starting_vals) == n_vars
            self.__problem.addVarGroup(name,          
                                    n_vars,
                                    type,
                                    lower=lower,
                                    upper=upper,
                                    value=starting_vals,
                                    )
        else:
            self.__problem.addVarGroup(name,          
                                    n_vars,
                                    type,
                                    lower=lower,
                                    upper=upper,
                                    )



    def add_constraint(self, name:str, lower:float|None, upper:float|None) -> None:
        '''
        ### How constraints work
        - if value > upper_bound --> **violated**
        - if value < lower_bound --> **violated**
        '''
        self.__problem.addCon(
                name,
                lower=lower,
                upper=upper,
            )
        

    def add_constraint_group(self, name:str, n_vars:int, lower:float|None, upper:float|None) -> None:
        '''
        ### How constraints work
        - if value > upper_bound --> **violated**
        - if value < lower_bound --> **violated**
        '''
        self.__problem.addConGroup(
                name,
                n_vars,
                lower=lower,
                upper=upper,
            )


    def init_problem(self, obj_function, problem_name:str="Optimization Problem") -> None:
        '''
        Initializes the problem
        '''
        self.__problem = Optimization(problem_name, obj_function)
        self.__problem.addObj("OBJ")
        self.__optimizer = OPT("ipopt")


    def solve(self, sens:str="FD", quiet:bool|None=None) -> None:
        '''
        Solves the problem.
        '''
        self.quiet(quiet=quiet)
        self.__sol = self.__optimizer(self.__problem, sens=sens)
        # solution exists but it has some oddities
        if (self.__sol.optInform['value'] in [-1,-3]) and (not self.quiet()):
            print(f"Solver message: {self.__sol.optInform['text']}")
        elif self.__sol.optInform['value'] not in [0, 1]:
            raise EnvironmentError(f"Model could not solve the optimization problem. It returned code:\n{self.__sol.optInform}\nWith the following solution instead: \n{self.__sol.xStar}")
        if not self.quiet():
            self.print_solution()


    def print_solution(self) -> None:
        print(self.__sol)


    def solution(self) -> dict[int,float]:
        '''
        Returns the values for the variables found by the solver.
        '''
        self.__weights:dict = dict()
        for var_idx in range(len(self.__sol.xStar['VARs'])):
            self.__weights[var_idx] = self.__sol.xStar['VARs'][var_idx]
        return self.__weights


    
