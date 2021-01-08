from pydantic import BaseModel
from datetime import date


class UserBase(BaseModel):
    nome: str
    data_nascimento: date
    cpf: str
    cep: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    rua: str
    bairro: str
    cidade: str
    estado: str

    class Config:
        orm_mode = True