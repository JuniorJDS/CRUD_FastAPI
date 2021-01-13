from schemas.user import UserAdress
from db import users, database

async def crete_post(user: UserAdress):
    query = users.insert().values(**user.dict())
    return await database.execute(query)

async def get_cpf(cpf: str):
    query = users.select().where(cpf==users.c.cpf)
    return await database.fetch_one(query=query)


async def get_all():
    query = users.select()
    return await database.fetch_all(query=query)

