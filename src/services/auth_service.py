from datetime import timedelta
from fastapi import HTTPException, status
from core.config import settings
from core.security import create_access_token, authenticate_user, create_user
from schemas.user_schema import UserResponse, UserCreate
from sqlalchemy.orm import Session

ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

def login_user(form_data, db: Session) -> dict: # Alterado o tipo de retorno
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Payload para ambos os tokens
    token_data = {"sub": user.username, "id": user.id}

    # 1. Criar o Access Token (curta duração)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data=token_data,
        expires_delta=access_token_expires
    )
    
    # 3. Retornar token
    return access_token


def register_user_service(user: UserCreate, db: Session):
    try:
        db_user = create_user(db, user)
        return UserResponse(
            username=db_user.username,
            email=db_user.email,
            full_name=db_user.full_name
        )
    except ValueError as e:
        print("Erro de valor ao criar usuário:", e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        print("erro ao criar usuário:", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao criar usuário"
        )