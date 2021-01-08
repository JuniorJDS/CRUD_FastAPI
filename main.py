from fastapi import FastAPI
from config import settings
from routers.v1 import user_v1
from models import user_models
from database import engine

user_models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(user_v1.router, prefix=settings.API_V1)