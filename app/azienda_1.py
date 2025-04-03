from __future__ import annotations # allows typing of class inside the same class
from enum import *

from typing import Any
import datetime

# UTILS
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
    
    def __eq__(self, other:link) -> bool:
        if other is None or \
            not isinstance(other, type(self)) or \
            type(self.obj_1()) != type(other.obj_1()) or \
            type(self.obj_2()) != type(other.obj_2()) or \
            hash(self) != hash(other):
            return False
        else:
            return ( self.obj_1() is other.obj_1() ) and ( self.obj_2() is other.obj_2() )
        




# TYPES
class Genere(StrEnum):
    uomo = auto()
    donna = auto()


# DOMAINS
class intGEZ():
    def __init__(self, i:int):
        if i < 0:
            raise ValueError(f"Value must be >= 0, now {i}.")
        self._i:int = i
    
    def value(self) -> int:
        return self._i
    
    def __hash__(self) -> int:
        return hash(self.value())
    
    def __eq__(self, other:intGEZ|int) -> bool:
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(other) != hash(self):
            return False
        elif isinstance(other, int):
            return self.value() == other
        else:
            return self.value() == other.value()
        
    def __lt__(self, other:intGEZ|int) -> bool:
        if isinstance(other, int):
            return self.value() < other
        elif isinstance(other, type(self)):
            return self.value() < other.value()
        else:
            raise TypeError(f"Operator < not defined between intGEZ and {type(other)}")
        
    def __gt__(self, other:intGEZ|int) -> bool:
        if isinstance(other, int):
            return self.value() > other
        elif isinstance(other, type(self)):
            return self.value() > other.value()
        else:
            raise TypeError(f"Operator > not defined between intGEZ and {type(other)}")
        
    def __le__(self, other:intGEZ|int) -> bool:
        if isinstance(other, int):
            return self.value() <= other
        elif isinstance(other, type(self)):
            return self.value() <= other.value()
        else:
            raise TypeError(f"Operator <= not defined between intGEZ and {type(other)}")
    
    def __le__(self, other:intGEZ|int) -> bool:
        if isinstance(other, int):
            return self.value() >= other
        elif isinstance(other, type(self)):
            return self.value() >= other.value()
        else:
            raise TypeError(f"Operator >= not defined between intGEZ and {type(other)}")
        
    def __add__(self, other:intGEZ|int) -> bool:
        if isinstance(other, int):
            return self.value() + other
        elif isinstance(other, type(self)):
            return self.value() + other.value()
        else:
            raise TypeError(f"Operator + not defined between intGEZ and {type(other)}")
    
    def __mul__(self, other:intGEZ|int) -> bool:
        if isinstance(other, int):
            return self.value() * other
        elif isinstance(other, type(self)):
            return self.value() * other.value()
        else:
            raise TypeError(f"Operator * not defined between intGEZ and {type(other)}")
        
    def __truediv__(self, other:intGEZ|int) -> bool:
        if isinstance(other, int):
            return self.value() / other
        elif isinstance(other, type(self)):
            return self.value() / other.value()
        else:
            raise TypeError(f"Operator / not defined between intGEZ and {type(other)}")


# OBJECTS
# TODO: must exist an afferenza link between every Impiegato and Dipartimento
class Impiegato():
    def __init__(self, nome:str, cognome:str, nascita:datetime.date, stipendio:intGEZ, data_afferenza:datetime.date, genere:Genere):
        if nome is None:
            raise ValueError(f"nome can't be None.")
        if cognome is None:
            raise ValueError(f"cognome can't be None.")
        if nascita is None:
            raise ValueError(f"nascita can't be None.")
        self._nome:str = nome
        self._cognome:str = cognome
        self._nascita:datetime.date = nascita
        self.set_stipendio(stipendio)
        self.set_data_afferenza(data_afferenza)
        self.set_genere(genere)

    
    # GETTER METHODS
    def nome(self) -> str:
        return self._nome 
    def cognome(self) -> str:
        return self._cognome
    def nascita(self) -> datetime.date:
        return self._nascita
    def stipendio(self) -> intGEZ:
        return self._stipendio
    def data_afferenza(self) -> datetime.date:
        return self._data_afferenza
    def genere(self) -> Genere:
        return self._genere
    

    # SETTER METHODS
    def set_stipendio(self, new_value:intGEZ) -> None:
        if new_value is None:
            raise ValueError(f"value can't be None.")
        self._stipendio = new_value
    def set_data_afferenza(self, new_value:datetime.date) -> None:
        if new_value is None:
            raise ValueError(f"value can't be None.")
        self._data_afferenza = new_value
    def set_genere(self, new_value:Genere) -> None:
        if new_value is None:
            raise ValueError(f"value can't be None.")
        self._genere = new_value


    # VIEW of OBJ (only has getter methods)
    class View():
        def __init__(self, obj:Impiegato):
            if obj is None:
                raise ValueError("obj can't be None")
            self._obj:Impiegato = obj
        def nome(self) -> str:
            return self._obj.nome() 
        def cognome(self) -> str:
            return self._obj.cognome()
        def nascita(self) -> datetime.date:
            return self._obj.nascita()
        def stipendio(self) -> intGEZ:
            return self._obj.stipendio()
        def data_afferenza(self) -> datetime.date:
            return self._obj._data_afferenza()
        def genere(self) -> Genere:
            return self._obj.genere()
        


class Progetto():
    def __init__(self, nome:str, budget:intGEZ):
        if nome is None:
            raise ValueError(f"nome can't be None.")
        self._nome:str = nome
        self.set_budget(budget)

    
    # GETTER METHODS
    def nome(self) -> str:
        return self._nome 
    def budget(self) -> str:
        return self._budget
    

    # SETTER METHODS
    def set_budget(self, new_value:intGEZ) -> None:
        if new_value is None:
            raise ValueError(f"value can't be None.")
        self._budget = new_value


    # VIEW of OBJ (only has getter methods)
    class View():
        def __init__(self, obj:Progetto):
            if obj is None:
                raise ValueError("obj can't be None")
            self._obj:Progetto = obj
        def nome(self) -> str:
            return self._obj.nome() 
        def budget(self) -> str:
            return self._obj.budget()
        


class Dipartimento():
    def __init__(self, nome:str, telefono:str):
        if nome is None:
            raise ValueError(f"nome can't be None.")
        self._nome:str = nome
        self.set_telefono(telefono)

    
    # GETTER METHODS
    def nome(self) -> str:
        return self._nome 
    def telefono(self) -> str:
        return self._telefono
    

    # SETTER METHODS
    def set_telefono(self, new_value:str) -> None:
        if new_value is None:
            raise ValueError(f"value can't be None.")
        self._telefono = new_value


    # VIEW of OBJ (only has getter methods)
    class View():
        def __init__(self, obj:Dipartimento):
            if obj is None:
                raise ValueError("obj can't be None")
            self._obj:Dipartimento = obj
        def nome(self) -> str:
            return self._obj.nome() 
        def telefono(self) -> str:
            return self._obj.telefono()




# ASSOCIATIONS
class afferenza():

    def __init__(self):
        self._afferenza:set[afferenza._link] = set()

    def afferenza(self) -> frozenset[afferenza._link]:
        return frozenset(self._afferenza)
    
    def add_link_afferenza(self, i:Impiegato, d:Dipartimento) -> None:
        l:afferenza._link = afferenza._link(i,d)
        # Can't have the same Impiegato in more than one link (1..1)
        for link in self.afferenza():
            if link.impiegato() == l.impiegato():
                raise ValueError(f"Cannot have multiple links for Impegato {i}.")
        self._afferenza.add(l)

    def remove_link_afferenza(self, l:afferenza._link) -> None:
        self._afferenza.remove(l)

    class _link(link):
        def __init__(self, impiegato:Impiegato, dipartimento:Dipartimento):
            self.super().__init__(impiegato, dipartimento)

        def impiegato(self) -> Impiegato:
            return self.obj_1()
        
        def dipartimento(self) -> Dipartimento:
            return self.obj_2()



class direzione():

    def __init__(self):
        self._direzione:set[direzione._link] = set()

    def direzione(self) -> frozenset[direzione._link]:
        return frozenset(self._direzione)
    
    def add_link_direzione(self, i:Impiegato, d:Dipartimento) -> None:
        l:direzione._link = direzione._link(i,d)
        # Can't have the same Impiegato in more than one link (0..1)
        # Can't have the same Dipartimento in more than one link (0..1=)
        for link in self.direzione():
            if link.impiegato() == l.impiegato():
                raise ValueError(f"Cannot have multiple links for Impegato {i}.")
            if link.dipartimento() == l.dipartimento():
                raise ValueError(f"Cannot have multiple links for Dipartimento {i}.")
        self._direzione.add(l)

    def remove_link_direzione(self, l:direzione._link) -> None:
        self._direzione.remove(l)

    class _link(link):
        def __init__(self, impiegato:Impiegato, dipartimento:Dipartimento):
            self.super().__init__(impiegato, dipartimento)

        def impiegato(self) -> Impiegato:
            return self.obj_1()
        
        def dipartimento(self) -> Dipartimento:
            return self.obj_2()
        



class imp_prog():

    def __init__(self):
        self._imp_prog:set[imp_prog._link] = set()

    def imp_prog(self) -> frozenset[imp_prog._link]:
        return frozenset(self._imp_prog)
    
    def add_link_imp_prog(self, i:Impiegato, p:Progetto) -> None:
        l:imp_prog._link = imp_prog._link(i,p)
        self._imp_prog.add(l)

    def remove_link_imp_prog(self, l:imp_prog._link) -> None:
        self._imp_prog.remove(l)

    class _link(link):
        def __init__(self, impiegato:Impiegato, progetto:Progetto):
            self.super().__init__(impiegato, progetto)

        def impiegato(self) -> Impiegato:
            return self.obj_1()
        
        def progetto(self) -> Progetto:
            return self.obj_2()




if __name__ == '__main__':
    pass