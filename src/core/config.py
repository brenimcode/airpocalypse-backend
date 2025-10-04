from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str = "your_api_key"
    api_secret: str = "your_api_secret"



settings = Settings()