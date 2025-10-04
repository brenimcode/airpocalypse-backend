from sqlalchemy import Column, String
from core.db import Base

class Inscrito(Base):
    __tablename__ = 'inscritos'

    email = Column(String, primary_key=True, unique=True, nullable=False)
    primeiro_nome = Column(String, nullable=False)

    def __repr__(self):
        return f"<Inscrito(email='{self.email}', primeiro_nome='{self.primeiro_nome}')>"
