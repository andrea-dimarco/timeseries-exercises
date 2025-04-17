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
from afferenza import *




class Impiegato():

    _nome:str
    _cognome:str
    _stipendio:str
    _afferenza:afferenza._link|None

    def __init__(self, *, nome:str, cognome:str, stipendio:PosReal):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_stipendio(stipendio)

    def __hash__(self) -> int:
        return hash( (self.nome(),self.cognome()) )

    def __eq__(self, value):
        pass

    def __repr__(self):
        return f"Impiegato(nome={self.nome()}, cognome={self.cognome()}, stipendio={self.stipendio()})"

    
    # GETTERS
    def nome(self) -> str:
        return self._nome
    def cognome(self) -> str:
        return self._cognome
    def stipendio(self) -> PosReal:
        return self._stipendio
    def afferenza(self) -> afferenza._link:
        return self._afferenza
    
    # SETTERS
    def set_nome(self, value:str) -> None:
        if not value:
            raise ValueError("'nome' can't be None.")
        self._nome = value
    def set_cognome(self, value:str) -> None:
        if not value:
            raise ValueError("'cognome' can't be None.")
        self._cognome = value
    def set_stipendio(self, value:PosReal) -> None:
        if not value:
            raise ValueError("'nome' can't be None.")
        self._stipendio = value
    def set_afferenza(self, dip:Dipartimento, data_afferenza:datetime.date) -> None:
        l = afferenza._link(imp=self, dip=dip, data_afferenza=data_afferenza)
        self._afferenza = l
        dip.add_link_afferenza(l=l)
    
    # OPERATIONS
    def progetto_a_budget_piu_alto(self) -> set[Progetto]:
        pass



if __name__ == '__main__':

    imp = Impiegato(nome="Andrea", cognome="Di Marco", stipendio=PosReal(10))
    dip = Dipartimento(nome="Informatica")

    
    print(imp)

    imp.set_afferenza(dip=dip, data_afferenza=None)