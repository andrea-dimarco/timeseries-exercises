# Internal Libraries
from __future__ import annotations # allows typing of class inside the same class
from abc import ABC, abstractmethod
from typing import Literal, Any
from enum import *
import datetime

# External Libraries
import numpy as np
import pandas as pd


# Imported Files
import utils
from types import *



class A(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_value(self) -> int:
        pass

    @abstractmethod
    def set_value(self) -> int:
        pass




class C(A):

    # constructor
    def __init__(self, value:float|int):
        self.set_value(value)

    # methods
    def get_value(self) -> float|int:
        return self.__value

    def set_value(self, value:float|int) -> float|int:
        if value is None:
            raise ValueError(f"value can't be None.")
        if not isinstance(value, (float,int)):
            raise TypeError(f"value must be float or int, not {type(value)}")
        self.__value:float|int = value

    class View:
        # only has getter methods
        # use this class when returning an object from a method so that the user can't edit the original object
        def __init__(self, obj:C):
            if obj is None:
                raise ValueError("obj can't be None")
            self._obj:C = obj
        
        def get_value(self) -> float|int:
            return self._obj.get_value()



class D(C):

    def __init__(self, value:float):
        if not isinstance(value, float):
            raise TypeError(f"value must be float, not {type(value)}")
        super().__init__(value)



class Associazione():

    def __init__(self):
        self._associazioni:set[Associazione._link] = set()

    def get_associazione(self) -> frozenset[Associazione._link]:
        return frozenset(self._associazioni)
    
    def add_link(self, obj1:Any, obj2:Any) -> None:
        self._associazioni.add(Associazione._link(obj1, obj2))

    def add_link(self, obj1:Any, obj2:Any) -> None:
        self._associazioni.remove(Associazione._link(obj1, obj2))

    class _link: # this models a single link
        def __init__(self, obj1:Any, obj2:Any):
            pass

        def set_obj1(self, obj1:Associazione._link) -> None:
            if obj1 is None:
                raise ValueError("obj1 can't be None")
            self._obj1:Any = obj1

        def set_obj2(self, obj2:Associazione._link) -> None:
            if obj2 is None:
                raise ValueError("obj can't be None")
            self._obj2:Any = obj2

        def get_obj1(self) -> Any:
            return self._obj1
        
        def get_obj2(self) -> Any:
            return self._obj2

        def __hash__(self):
            return hash(tuple(self.get_obj1(), self.get_obj2()))
            
        def __eq__(self, other):
            return (self.get_obj1() == other.get_obj1()) and (self.get_obj2() == other.get_obj2())

    




if __name__ == '__main__':
    
    # useful variables
    verbose:bool = True
    data_folder:str = "/data/"

    obj1 = C(1)
    obj2 = D(2.0)

    print(f"{C.View(obj1).get_value()}")

