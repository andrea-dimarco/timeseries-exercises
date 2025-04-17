# Internal Libraries
from __future__ import annotations # allows typing of class inside the same class
from abc import ABC, abstractmethod
from typing import *
from enum import *
import datetime


# Project Libraries
from utils import *
from PosInt import *
from Genere import *
from PosReal import *
from Progetto import *
from Dipartimento import *
from Impiegato import *


class afferenza:

    class _link(link):
        _impiegato:Impiegato
        _dipartiemnto:Dipartimento
        _data_afferenza:datetime.date

        def __init__(self, imp:Impiegato, dip:Dipartimento, data_afferenza:datetime.date):
            super().__init__(imp, dip)
            self._data_afferenza = data_afferenza
        
        def impiegato(self) -> Impiegato:
            return self.obj_1()
        
        def dipartimento(self) -> Dipartimento:
            return self.obj_2()
        
        def data_afferenza(self) -> datetime.date:
            return self._data_afferenza
        




if __name__ == '__main__':
    pass