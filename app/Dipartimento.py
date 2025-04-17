# Internal Libraries
from __future__ import annotations # allows typing of class inside the same class
from abc import ABC, abstractmethod
from typing import Literal, Any
from enum import *
import datetime


# Project Libraries
from utils import *
from PosInt import *
from Genere import *
from PosReal import *
from afferenza import *




class Dipartimento():

    _nome:str
    _affererenza:set[affererenza.link]

    def __init__(self, *, nome:str):
        self.set_nome(nome)

    def __hash__(self) -> int:
        return hash(self.nome())

    def __eq__(self, value):
        if type(self) != type(value) or hash(self) != hash(value):
            return False
        else:
            return self.nome() == value.nome()

    
    # GETTER
    def nome(self) -> str:
        return self._nome
    
    # SETTERS
    def set_nome(self, value:str) -> None:
        if not value:
            raise ValueError("'nome' can't be None.")
        self._nome = value

    # ASSOCIATIONS
    def add_link_afferenza(self, l:afferenza._link) -> None:
        if l.dipartimento() != self:
            raise ValueError("link does not belong to object!")
        if l.impiegato().afferenza() is None:
            l.impiegato().set_afferenza(l)
        self._affererenza.add(l)


if __name__ == '__main__':

    print("Hello")