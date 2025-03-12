import numpy as np
import pandas as pd



class AR:

    def __init__(self, p:int, c:float=0.0, mu:float=0.0, std:float=1.0):
        self.__p:int = p
        self.__phi:list[float] = list()
        self.__state:list[float] = list()
        for _ in range(p):
            self.__phi.append(0.0)
            self.__state.append(0.0)
        self.__c:float = c
        self.__mu:float = mu
        self.__std:float = std


    def state(self, new_state:list[float]|None=None) -> list[float]:
        '''
        Get (and set) the model state
        '''
        if not (new_state is None):
            assert len(new_state) == self.__p
            self.__state = new_state
        return self.__state
    

    def phi(self, new_phi:list[float]|None=None) -> list[float]:
        '''
        Get (and set) the model coefficients
        '''
        if not (new_phi is None):
            assert len(new_phi) == self.__p
            self.__phi = new_phi
        return self.__phi
    

    def c(self, new_c:float|None=None) -> float:
        '''
        Get (and set) the model coefficients
        '''
        if not (new_c is None):
            self.__c = new_c
        return self.__c


    def p(self) -> int:
        return self.__p


    def epsilon(self) -> float:
        return np.random.normal(loc=self.__mu, scale=self.__std)


    def run(self) -> float:
        yt:float = self.c() + self.epsilon()
        for i in range(self.p()):
            yt += self.state()[i]*self.phi()[i]
        return yt
    
    def forecast(self, steps:int) -> float:
        print("The forecast function is not supported yet")
        return 0.0
    

    def push_state(self, item:float) -> None:
        for i in range(self.p()-1):
            self.__state[i+1] = self.__state[i]
        self.__state[0] = item