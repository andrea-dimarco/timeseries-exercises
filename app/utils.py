# Internal Libraries
from __future__ import annotations # allows typing of class inside the same class
from enum import *
from typing import *

import datetime




class link:
    def __init__(self, obj_1:Any, obj_2:Any):
        if obj_1 is None:
            raise ValueError("obj_1 cannot be None.")
        if obj_2 is None:
            raise ValueError("obj_2 cannot be None.")
        self._obj_1 = obj_1
        self._obj_2 = obj_2

    def obj_1(self) -> Any:
        return self._obj1
    
    def obj_2(self) -> Any:
        return self.obj_2
    
    def __hash__(self):
        return hash(tuple(self.obj_1(), self.obj_2()))
    
    def __eq__(self, other:Self) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False
        else:
            return ( self.obj_1() is other.obj_1() ) and ( self.obj_2() is other.obj_2() )
        

class View():
    def __init__(self, obj:Any):
        if obj is None:
            raise ValueError("obj cannot be None.")
        self._obj:Any = obj
    def __hash__(self):
        return hash(self._obj)
    def __eq__(self, other):
        # TODO: we should be able to see 'True' if a view of an object is equal to the object!
        return self._obj == other
    








if __name__ == '__main__':

    pass



    
