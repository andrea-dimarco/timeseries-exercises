# Internal Libraries
from typing import *
from enum import *


class PosReal(float):

    def __new__(cls, v:int|float):
        if v < 0:
            raise ValueError("v must be >= 0")
        return float.__new__(cls, v)



if __name__ == '__main__':
    pass

    print(PosReal(3))