from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from core.config import settings
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
from schemas.user_schema import UserCreate
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session
from models.user import User
from core.db import get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_user(db: Session, user: UserCreate) -> User:
    # Verifica se o usuário já existe
    existing_user = get_user(user.username, db)
    if existing_user:
        raise ValueError("Username already exists")
    
    try:
        # Cria o hash da senha e o novo usuário
        hashed = pwd_context.hash(user.password)

    except Exception as e:
        print("Erro ao hashear a senha:", e)
        raise

    db_user = User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed,
        modalidade=user.modalidade,
        notificacoes_ativas=user.notificacoes_ativas,
        regiao_coordenadas=user.regiao_coordenadas,
        observacoes=user.observacoes
    )
   
    # Salva no banco de dados
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_user(username: str, db: Session) -> User | None:
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(email: str, db: Session) -> User | None:
    return db.query(User).filter(User.email == email).first()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str, db: Session) -> User | None:
    user = get_user(username, db)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
