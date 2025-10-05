from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
from datetime import datetime

class UserInsightsUpsert(BaseModel):
	user_email: EmailStr
	insight_geral: str
	iqa_valor: str  # Bom, Muito Bom, Moderado, Ruim
	detalhes_do_ar: Dict[str, Any]
	insights_ia_detalhes: Dict[str, Any]
