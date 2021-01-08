from sqlalchemy import Column, Integer, String, Date
from database import Base

class User(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(30), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    cpf = Column(String(11), nullable=False)
    cep = Column(String(8), nullable=False)

    rua = Column(String(100))
    bairro = Column(String(80))
    cidade = Column(String(80))
    estado = Column(String(20))
