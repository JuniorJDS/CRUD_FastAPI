from starlette.testclient import TestClient
from config import settings
from main import app
import json


client = TestClient(app)

def test_get_hello():
    response = client.get(f"{settings.API_V1}/user")
    assert response.status_code == 200

def test_post_user():
    user = {"nome": "nome1", "data_nascimento": 20, "cpf": "12212233687", "cep": "27327150"}

    response = client.post(f"{settings.API_V1}/user", data=json.dumps(user))
    assert response.status_code == 201
