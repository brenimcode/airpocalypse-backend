from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.core.config import get_settings
from src.core.db import init_db
from src.routers import users_router

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando...")
    init_db()
    print("Conectado!")
    yield
    print("Encerrando...")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="API REST para gerenciamento de inscritos do chatbot",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix=settings.API_V1_STR)
