from pydantic import BaseModel, EmailStr
from typing import Optional, List, TypedDict

class UserResponse(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: Optional[str] = None
    modalidade: Optional[str] = "Esporte ao ar livre"
    notificacoes_ativas: Optional[bool] = True
    regiao_coordenadas: Optional[str] = None
    observacoes: Optional[str] = None

class UserInDB():
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None