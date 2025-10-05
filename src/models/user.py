from core.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    modalidade = Column(String, nullable=True, doc="Modalidade de esporte, ex: natação, corrida")
    notificacoes_ativas = Column(Boolean, nullable=False, default=1, doc="True=ativo, False=inativo")
    regiao_coordenadas = Column(String, nullable=True, doc="Coordenadas da região em formato texto")
    observacoes = Column(String, nullable=True, doc="Campo livre para observações/notas do usuário")
    created_at = Column(DateTime, nullable=False, server_default=func.now())

