from __future__ import annotations # allows typing of class inside the same class
from enum import *

from typing import Any
import datetime

# UTILS
class link():
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
    




# TYPES
class Genere(Enum):
    uomo = auto()
    donna = auto()


# DOMAINS
class IntGEZ():
    def __init__(self, i:int):
        if i is None:
            raise ValueError("Value cannot be None.")
        elif i < 0:
            raise ValueError(f"Value must be >= 0, now {i}.")
        self._i:int = i
    
    def value(self) -> int:
        return self._i
    
    def __hash__(self) -> int:
        return hash(self.value())
    
    def __eq__(self, other:IntGEZ) -> bool:
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(other) != hash(self):
            return False
        elif isinstance(other, int):
            return self.value() == other
        else:
            return self.value() == other.value()
        
    def __lt__(self, other:IntGEZ|int) -> bool:
        if isinstance(other, int):
            return self.value() < other
        elif isinstance(other, type(self)):
            return self.value() < other.value()
        else:
            raise TypeError(f"Operator < not defined between IntGEZ and {type(other)}")
        
    def __gt__(self, other:IntGEZ|int) -> bool:
        if isinstance(other, int):
            return self.value() > other
        elif isinstance(other, type(self)):
            return self.value() > other.value()
        else:
            raise TypeError(f"Operator > not defined between IntGEZ and {type(other)}")
        
    def __le__(self, other:IntGEZ|int) -> bool:
        if isinstance(other, int):
            return self.value() <= other
        elif isinstance(other, type(self)):
            return self.value() <= other.value()
        else:
            raise TypeError(f"Operator <= not defined between IntGEZ and {type(other)}")
    
    def __ge__(self, other:IntGEZ|int) -> bool:
        if isinstance(other, int):
            return self.value() >= other
        elif isinstance(other, type(self)):
            return self.value() >= other.value()
        else:
            raise TypeError(f"Operator >= not defined between IntGEZ and {type(other)}")
        
    def __add__(self, other:IntGEZ|int) -> IntGEZ: 
        if isinstance(other, int):
            return IntGEZ(self.value() + other)
        elif isinstance(other, type(self)):
            return IntGEZ(self.value() + other.value())
        else:
            raise TypeError(f"Operator + not defined between IntGEZ and {type(other)}")
    
    def __mul__(self, other:IntGEZ|int) -> IntGEZ:
        if isinstance(other, int):
            return IntGEZ(self.value() * other)
        elif isinstance(other, type(self)):
            return self.value() * other.value()
        else:
            raise TypeError(f"Operator * not defined between IntGEZ and {type(other)}")
        
    def __truediv__(self, other:IntGEZ|int) -> float:
        if isinstance(other, int):
            return self.value() / other
        elif isinstance(other, type(self)):
            return self.value() / other.value()
        else:
            raise TypeError(f"Operator / not defined between IntGEZ and {type(other)}")



# OBJECTS
_IMPIEGATO_DB:dict[str,Impiegato] = dict()
_PROGETTO_DB:set[Progetto] = set()
_DIPARTIMENTO_DB:dict[str,Impiegato] = dict()

# TODO: must exist an afferenza link between every Impiegato and Dipartimento
class Impiegato():

    def create_impiegato(id:str, nome:str, cognome:str, nascita:datetime.date, stipendio:IntGEZ, data_afferenza:datetime.date, genere:Genere) -> None:
        if not id in _IMPIEGATO_DB:
            o:Impiegato = Impiegato(id, nome, cognome, nascita, stipendio, data_afferenza, genere)
            _IMPIEGATO_DB[id] = o
        else:
            raise KeyError(f"Object with id {id} already exists.")

    def get_impiegato(id:str) -> Impiegato.View:
        return Impiegato.View(_IMPIEGATO_DB[id])

    def __init__(self, id:str, nome:str, cognome:str, nascita:datetime.date, stipendio:IntGEZ, data_afferenza:datetime.date, genere:Genere):
        if id is None:
            raise ValueError(f"id cannot be None.")
        if nome is None:
            raise ValueError(f"nome cannot be None.")
        if cognome is None:
            raise ValueError(f"cognome cannot be None.")
        if nascita is None:
            raise ValueError(f"nascita cannot be None.")
        self._id:str = id
        self._nome:str = nome
        self._cognome:str = cognome
        self._nascita:datetime.date = nascita
        self.set_stipendio(stipendio)
        self.set_data_afferenza(data_afferenza)
        self.set_genere(genere)

    
    # GETTER METHODS
    def id(self) -> str:
        return self._id
    def nome(self) -> str:
        return self._nome 
    def cognome(self) -> str:
        return self._cognome
    def nascita(self) -> datetime.date:
        return self._nascita
    def stipendio(self) -> IntGEZ:
        return self._stipendio
    def data_afferenza(self) -> datetime.date:
        return self._data_afferenza
    def genere(self) -> Genere:
        return self._genere
    

    # SETTER METHODS
    def set_stipendio(self, new_value:IntGEZ) -> None:
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


    # REQUIRED
    def __hash__(self):
        return hash(self.id())


    # VIEW of OBJ (only has getter methods)
    class View(View):
        def nome(self) -> str:
            return self._obj.nome() 
        def cognome(self) -> str:
            return self._obj.cognome()
        def nascita(self) -> datetime.date:
            return self._obj.nascita()
        def stipendio(self) -> IntGEZ:
            return self._obj.stipendio()
        def data_afferenza(self) -> datetime.date:
            return self._obj._data_afferenza()
        def genere(self) -> Genere:
            return self._obj.genere()
        


class Progetto():

    def create_progetto(nome:str, budget:IntGEZ):
        obj:Progetto = Progetto(nome, budget)
        _PROGETTO_DB.add(obj)

    def get_progetto_db() -> frozenset[Progetto]:
        return frozenset(_PROGETTO_DB)

    def __init__(self, nome:str, budget:IntGEZ):
        if nome is None:
            raise ValueError(f"nome cannot be None.")
        self._nome:str = nome
        self.set_budget(budget)

    
    # GETTER METHODS
    def nome(self) -> str:
        return self._nome 
    def budget(self) -> str:
        return self._budget
    

    # SETTER METHODS
    def set_budget(self, new_value:IntGEZ) -> None:
        if new_value is None:
            raise ValueError(f"value can't be None.")
        self._budget = new_value

    
    # REQUIRED
    def __hash__(self):
        return hash(self.nome())


    # VIEW of OBJ (only has getter methods)
    class View(View):
        def nome(self) -> str:
            return self._obj.nome() 
        def budget(self) -> str:
            return self._obj.budget()
        


class Dipartimento():

    def create_dipartimento(nome:str, telefono:str) -> None:
        if nome in _DIPARTIMENTO_DB:
            raise KeyError(f"Object with is {nome} already exists.")
        else:
            _DIPARTIMENTO_DB[nome] = Dipartimento(nome, telefono)
    
    def get_dipartimento(nome:str) -> Dipartimento.View:
        return Dipartimento.View(_DIPARTIMENTO_DB[nome])

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
    

    # REQUIRED
    def __hash__(self):
        return hash(self.nome())

    def __eq__(self, other:Any):
        if other is None or \
            hash(self) != hash(other):
            return False
        else:
            return self.nome() == other.nome()


    # VIEW of OBJ (only has getter methods)
    class View(View):
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
    Impiegato.create_impiegato(id="0",
                               nome="Alessio",
                               cognome="Rossi",
                               nascita="",
                               stipendio=IntGEZ(50),
                               data_afferenza="",
                               genere=Genere.uomo
                              )
    Impiegato.create_impiegato(id="1",
                               nome="Bianca",
                               cognome="Gialli",
                               nascita="",
                               stipendio=IntGEZ(200),
                               data_afferenza="",
                               genere=Genere.donna
                              )

    Dipartimento.create_dipartimento(nome="Informatica", telefono="55512345")

    i:Impiegato.View = Impiegato.get_impiegato(id="0")
    d:Dipartimento.View = Dipartimento.get_dipartimento(nome="Informatica")

    # AFFERENZA_DB:afferenza = afferenza()

    # AFFERENZA_DB.add_link_afferenza(i,d)

    print(type(5 / 1))

