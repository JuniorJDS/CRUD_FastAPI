from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1: str = "/api/v1"


settings = Settings()