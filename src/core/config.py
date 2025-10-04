from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_key: str = "your_api_key"
    api_secret: str = "your_api_secret"

    # Database (sua URL importante)
    DATABASE_URL: str = "postgresql://postgres:123@localhost:5433/postgres"

    # API Settings (campos que estavam faltando)
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Chatbot API"

    # Security
    SECRET_KEY: str = "sua-chave-secreta-aqui-mude-em-producao"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()  # Corrigido: usar get_settings() em vez de Settings()