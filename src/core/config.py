from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str = "your_api_key"
    api_secret: str = "your_api_secret"
    DATABASE_URL: str = "postgresql://postgres:123@localhost:5433/postgres"
    


settings = Settings()