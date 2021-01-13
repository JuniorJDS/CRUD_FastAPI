from fastapi import FastAPI
from config import settings
from routers.v1 import user_v1
# from models import user_models
# from database import engine
from db import database, metadata, engine
metadata.create_all(engine)

# user_models.Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

app.include_router(user_v1.router, prefix=settings.API_V1)