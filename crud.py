from schemas.user import UserAdress
from db import users, database

async def crete_post(user: UserAdress):
    query = users.insert().values(**user.dict())
    return await database.execute(query)