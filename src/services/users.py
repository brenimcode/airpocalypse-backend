from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional
from src.models.subscriber import Inscrito
from src.schemas.user import InscritoCreate, InscritoUpdate


class InscritoService:
    #Adicionar inscrito
    @staticmethod
    def create(db: Session, inscrito_data: InscritoCreate) -> Inscrito:
        # Verifica se email já existe
        existing = db.query(Inscrito).filter(
            Inscrito.email == inscrito_data.email
        ).first()

        if existing:
            raise ValueError(f"Email {inscrito_data.email} já cadastrado")

        inscrito = Inscrito(**inscrito_data.model_dump())
        db.add(inscrito)
        db.commit()
        db.refresh(inscrito)
        return inscrito

    # Buscar inscrito por ID
    @staticmethod
    def get_by_id(db: Session, inscrito_id: int) -> Optional[Inscrito]:
        return db.query(Inscrito).filter(Inscrito.id == inscrito_id).first()

    # Buscar inscrito por Email
    @staticmethod
    def get_by_email(db: Session, email: str) -> Optional[Inscrito]:
        return db.query(Inscrito).filter(Inscrito.email == email).first()

    # Buscar inscritos -> Obs.: Paginei isso aí, Brenão.
    @staticmethod
    def get_all(
            db: Session,
            skip: int = 0,
            limit: int = 100,
            search: Optional[str] = None
    ) -> tuple[list[Inscrito], int]:
        query = db.query(Inscrito)

        # Filtro de busca
        if search:
            query = query.filter(
                or_(
                    Inscrito.nome.ilike(f"%{search}%"),
                    Inscrito.email.ilike(f"%{search}%")
                )
            )

        total = query.count()
        items = query.offset(skip).limit(limit).all()

        return items, total

    # Atualizar os dados de um inscrito
    @staticmethod
    def update(
            db: Session,
            inscrito_id: int,
            inscrito_data: InscritoUpdate
    ) -> Optional[Inscrito]:
        inscrito = db.query(Inscrito).filter(Inscrito.id == inscrito_id).first()

        if not inscrito:
            return None

        update_data = inscrito_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(inscrito, field, value)

        db.commit()
        db.refresh(inscrito)
        return inscrito

    # Remover um inscrito
    @staticmethod
    def delete(db: Session, inscrito_id: int) -> bool:
        inscrito = db.query(Inscrito).filter(Inscrito.id == inscrito_id).first()

        if not inscrito:
            return False

        db.delete(inscrito)
        db.commit()
        return True
