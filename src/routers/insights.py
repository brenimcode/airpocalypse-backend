from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.db import get_db
from services.insights_service import upsert_user_insights_service, get_user_insights_service
from schemas.insight_schema import UserInsightsUpsert


router = APIRouter()

@router.post("/upsert/{user_email}", status_code=201)
def upsert_user_insights(insights_data: UserInsightsUpsert, db: Session = Depends(get_db)):
	"""
	Upsert: recebe dados de insights e insere ou atualiza no banco.
	"""
	try:
		return upsert_user_insights_service(insights_data, db)
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))

@router.get("/{user_email}")
def get_user_insights(user_email: str, db: Session = Depends(get_db)):
	"""
	Get: retorna os insights salvos para o dashboard do usuário.
	"""
	insights = get_user_insights_service(user_email, db)
	if not insights:
		raise HTTPException(status_code=404, detail="Insights não encontrados para este usuário.")
	return insights
