from fastapi import APIRouter, Response, Request, Depends
from schemas.user_schema import UserResponse
from sqlalchemy.orm import Session
from core.db import get_db
from fastapi.security import OAuth2PasswordRequestForm
from services.auth_service import login_user, register_user_service
from schemas.user_schema import UserCreate

router = APIRouter()

@router.post(
    "/login",
    description="Autentica o usuário e usa token JWT."
)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    token = login_user(form_data, db)
    return {"status": "success", "bearer_token": token}


@router.post("/register", response_model=UserResponse, status_code=201)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return register_user_service(user, db)