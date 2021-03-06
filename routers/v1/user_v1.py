from fastapi import APIRouter, Depends, HTTPException
from schemas import user
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from sqlalchemy.orm import Session
from routers import deps
from services import user_services
from pycep_correios import get_address_from_cep
import aiohttp
import asyncio
from aiohttp import ClientSession
from crud import crete_post, get_cpf, get_all
from typing import List


router = APIRouter(
    prefix = "/user"
)

@router.on_event('startup')
async def startup_event():
    global session
    session = aiohttp.ClientSession()

@router.on_event('shutdown')
async def shutdown_event():
    await session.close()



@router.get("", response_model=List[user.UserCreate])
async def get_hello():
    return await get_all()

async def get_cep(user):
    '''
        Consulta o cep, se válido, retorna o endereço.
    '''
    async with session.get(f"http://viacep.com.br/ws/{user.cep}/json") as response:
        result = await response.json()
        if result.get('erro'):
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="CEP inválido ou não encontrado.")
    return result


@router.post("", status_code=HTTP_201_CREATED)#, response_model=user.User)
async def create_user(user:user.UserAdress, db: Session = Depends(deps.get_db)):
    user_db = None# user_services.get_user_cpf(db, cpf= user.cpf)
    if user_db:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="CPF already registered")

    endereco = await get_cep(user)

    user.rua = endereco.get('logradouro')
    user.bairro = endereco.get('bairro')
    user.cidade = endereco.get('localidade')
    user.estado = endereco.get('uf')
    
    return user #user_services.create_user(db=db, user=user)


# primeiro teste com database assincronomo
@router.post("/teste", status_code=HTTP_201_CREATED)
async def new_user(user: user.UserAdress):
    user_db = await get_cpf(user.cpf)
    if user_db:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="CPF already registered")

    endereco = await get_cep(user)

    user.rua = endereco.get('logradouro')
    user.bairro = endereco.get('bairro')
    user.cidade = endereco.get('localidade')
    user.estado = endereco.get('uf')

    user_id = await crete_post(user)

    response_object = {
        "id": user_id,
        **user.dict()
    }
    
    return response_object
