from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:123@localhost:5433/postgres"
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60



settings = Settings()