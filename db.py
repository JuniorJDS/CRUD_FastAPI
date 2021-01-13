from sqlalchemy import create_engine, MetaData, Column, String, Date, Table, Integer
from databases import Database

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:root@127.0.0.1:5432/cad_db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()

users = Table(
    'usuario',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, nullable=False),
    Column('nome', String, nullable=False),
    Column('data_nascimento', Date, nullable=False),
    Column('cpf', String, nullable=False),
    Column('cep', String, nullable=False),

    Column('rua', String),
    Column('bairro', String),
    Column('cidade', String),
    Column('estado', String)
)

database = Database(SQLALCHEMY_DATABASE_URL)