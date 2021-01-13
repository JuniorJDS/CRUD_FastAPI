from pydantic import BaseModel, validator, ValidationError
from datetime import date
from typing import Optional
import re


class UserBase(BaseModel):
    nome: str
    data_nascimento: date
    cpf: str
    cep: str

    #@validator('cep')
    #def cep_validator(cls, v):
        #regex = re.compile('^\d{8}$')

        #assert regex.match(v), 'CEP com Formato inválido.'
        #return v

class UserCreate(UserBase):
    pass

class UserAdress(UserBase):
    rua: Optional[str]
    bairro: Optional[str] 
    cidade: Optional[str] 
    estado: Optional[str]

class User(UserBase):
    id: int
    rua: str = None
    bairro: str = None
    cidade: str = None
    estado: str = None

    class Config:
        orm_mode = True
