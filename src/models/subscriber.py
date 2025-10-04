from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from src.core.db import Base


class Inscrito(Base):
    __tablename__ = 'inscritos'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False, index=True)
    nome = Column(String, nullable=False)
    escopo = Column(String, default="Indefinido")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Inscrito(id={self.id}, email='{self.email}', nome='{self.nome}')>"