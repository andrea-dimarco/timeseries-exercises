# Internal Libraries
from __future__ import annotations # allows typing of class inside the same class
from abc import ABC, abstractmethod
from typing import *
from enum import *
import datetime


class PosInt(int):

    def __new__(cls, v:int|float|Self) -> Self:
        if v < 0:
            raise ValueError("v must be >= 0")
        return int.__new__(cls, v)



if __name__ == '__main__':
    pass

    print(PosInt(3))