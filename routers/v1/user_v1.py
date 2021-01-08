from fastapi import APIRouter, Depends, HTTPException
from schemas import user
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from sqlalchemy.orm import Session
from routers import deps
from services import user_services


router = APIRouter(
    prefix = "/user"
)

@router.get("")
async def get_hello():
    return {'message': 'Hello World version 1'}

@router.post("", status_code=HTTP_201_CREATED)
async def create_user(user:user.UserCreate, db: Session = Depends(deps.get_db)):
    user_db = user_services.get_user_cpf(db, cpf= user.cpf)
    if user_db:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="CPF already registered")
    return user_services.create_user(db=db, user=user)
