from __future__ import annotations # allows typing of class inside the same class
from enum import *


import datetime



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
class Impiegato():
    def __init__(self, nome:str, cognome:str, nascita:datetime.date, stipendio:intGEZ, data_afferenza:datetime.date, genere:Genere):
        self._nome:str = nome
        self._cognome:str = cognome
        self._nascita:datetime.date = nascita
        self._stipendio:intGEZ = stipendio
        self._data_afferenza:datetime.date = data_afferenza
        self._genere:Genere = genere

    
    # GETTER METHODS
    def get_nome(self) -> str:
        return self._nome 
    def get_cognome(self) -> str:
        return self._cognome
    def get_nascita(self) -> datetime.date:
        return self._nascita
    def get_stipendio(self) -> intGEZ:
        return self._stipendio
    def get_data_afferenza(self) -> datetime.date:
        return self._data_afferenza
    def get_genere(self) -> Genere:
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
        def get_nome(self) -> str:
            return self._obj.get_nome() 
        def get_cognome(self) -> str:
            return self._obj.get_cognome()
        def get_nascita(self) -> datetime.date:
            return self._obj.get_nascita()
        def get_stipendio(self) -> intGEZ:
            return self._obj.get_stipendio()
        def get_data_afferenza(self) -> datetime.date:
            return self._obj._data_afferenza()
        def get_genere(self) -> Genere:
            return self._obj.get_genere()
        


class Progetto():
    def __init__(self, nome:str, budget:intGEZ):
        self._nome:str = nome
        self._budget:intGEZ = budget

    
    # GETTER METHODS
    def get_nome(self) -> str:
        return self._nome 
    def get_budget(self) -> str:
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
        def get_nome(self) -> str:
            return self._obj.get_nome() 
        def get_budget(self) -> str:
            return self._obj.get_budget()
        


class Dipartimento():
    def __init__(self, nome:str, telefono:str):
        self._nome:str = nome
        self._telefono:str = telefono

    
    # GETTER METHODS
    def get_nome(self) -> str:
        return self._nome 
    def get_telefono(self) -> str:
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
        def get_nome(self) -> str:
            return self._obj.get_nome() 
        def get_telefono(self) -> str:
            return self._obj.get_telefono()




# ASSOCIATIONS




if __name__ == '__main__':
    pass