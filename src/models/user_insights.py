from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from core.db import Base

class UserInsights(Base):
	__tablename__ = 'user_insights'

	id = Column(Integer, primary_key=True, autoincrement=True)
	user_email = Column(String(255), ForeignKey('users.email'), unique=True, nullable=False, doc="E-mail do usuário, chave estrangeira para Users")
	insight_geral = Column(Text, nullable=False, doc="Resumo das recomendações da IA para o dia")
	data_atualizacao = Column(DateTime, nullable=False, server_default=func.now(), doc="Data/hora do último cálculo dos insights")
	iqa_valor = Column(Text, nullable=False, doc="Valor do IQA: Bom, Muito Bom, Moderado, Ruim")
	detalhes_do_ar = Column(JSONB, nullable=True, doc="Dados brutos/semi-estruturados da qualidade do ar")
	insights_ia_detalhes = Column(JSONB, nullable=True, doc="Estrutura de insights específicos por modalidade")
