from sqlalchemy.orm import Session
from models.user_insights import UserInsights
from datetime import datetime, timezone
from schemas.insight_schema import UserInsightsUpsert


def upsert_user_insights_service(insights_data: UserInsightsUpsert, db: Session):
    """
    Insere ou atualiza os insights do usuário no banco.
    insights_data deve conter pelo menos 'user_email'.
    """
    user_email = insights_data.user_email
    
    # Validação do e-mail
    if not user_email:
        raise ValueError("user_email é obrigatório para upsert de insights.")

    # 1. Preparar dados para update/insert
    update_data = insights_data.model_dump(
        exclude_unset=True,  # Exclui campos que não foram passados (Pydantic v2)
        exclude={'user_email'} # O email é a chave, não deve ser atualizado
    )
    
    # Garante que o timestamp seja atualizado com a zona UTC
    update_data['data_atualizacao'] = datetime.now(timezone.utc)
    
    # Converte os campos JSON que são Pydantic para dict
    if 'detalhes_do_ar' in update_data:
        update_data['detalhes_do_ar'] = dict(update_data['detalhes_do_ar'])
    if 'insights_ia_detalhes' in update_data:
        update_data['insights_ia_detalhes'] = dict(update_data['insights_ia_detalhes'])

    # 2. Tenta encontrar a instância existente
    instance_query = db.query(UserInsights).filter(UserInsights.user_email == user_email)
    instance = instance_query.first()
    
    if instance:
        # 3. Atualiza (melhor performance: usa o método update() do Query)
        instance_query.update(update_data, synchronize_session="fetch")
        
        # O refresh ainda é necessário para obter o objeto atualizado no Python
        db.refresh(instance)
    else:
        # 4. Insere
        # Adiciona o user_email de volta aos dados para a criação
        create_data = update_data
        create_data['user_email'] = user_email 
        
        instance = UserInsights(**create_data)
        db.add(instance)

    db.commit()
    db.refresh(instance)
    return instance

def get_user_insights_service(user_email: str, db: Session):
	"""
	Busca os insights do usuário pelo e-mail.
	"""
	return db.query(UserInsights).filter_by(user_email=user_email).first()
