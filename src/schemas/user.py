from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class InscritoCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    origem: Optional[str] = Field("chatbot", max_length=50)

class InscritoUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None

class InscritoResponse(BaseModel):
    id: int
    nome: str
    email: str
    origem: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

class InscritoList(BaseModel):
    total: int
    items: list[InscritoResponse]
