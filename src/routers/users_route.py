from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import Optional

from src.core.db import get_db
from src.services.users import InscritoService
from src.schemas.user import (
    InscritoCreate,
    InscritoUpdate,
    InscritoResponse,
    InscritoList
)

router = APIRouter(
    prefix="/inscritos",
    tags=["Inscritos"]
)


@router.post(
    "/",
    response_model=InscritoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar novo inscrito"
)
def create_inscrito(
        inscrito: InscritoCreate,
        db: Session = Depends(get_db)
):
    try:
        return InscritoService.create(db, inscrito)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=InscritoList,
    summary="Listar inscritos"
)
def list_inscritos(
        skip: int = Query(0, ge=0, description="Número de registros para pular"),
        limit: int = Query(100, ge=1, le=1000, description="Máximo de registros"),
        search: Optional[str] = Query(None, description="Buscar por nome ou email"),
        db: Session = Depends(get_db)
):
    items, total = InscritoService.get_all(db, skip, limit, search)
    return {"total": total, "items": items}


@router.get(
    "/{inscrito_id}",
    response_model=InscritoResponse,
    summary="Buscar inscrito por ID"
)
def get_inscrito(
        inscrito_id: int,
        db: Session = Depends(get_db)
):
    inscrito = InscritoService.get_by_id(db, inscrito_id)

    if not inscrito:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Inscrito com ID {inscrito_id} não encontrado"
        )

    return inscrito


@router.get(
    "/email/{email}",
    response_model=InscritoResponse,
    summary="Buscar inscrito por email"
)
def get_inscrito_by_email(
        email: str,
        db: Session = Depends(get_db)
):
    inscrito = InscritoService.get_by_email(db, email)

    if not inscrito:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Inscrito com email {email} não encontrado"
        )

    return inscrito


@router.put(
    "/{inscrito_id}",
    response_model=InscritoResponse,
    summary="Atualizar inscrito"
)
def update_inscrito(
        inscrito_id: int,
        inscrito_data: InscritoUpdate,
        db: Session = Depends(get_db)
):
    inscrito = InscritoService.update(db, inscrito_id, inscrito_data)

    if not inscrito:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Inscrito com ID {inscrito_id} não encontrado"
        )

    return inscrito


@router.delete(
    "/{inscrito_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deletar inscrito"
)
def delete_inscrito(
        inscrito_id: int,
        db: Session = Depends(get_db)
):
    success = InscritoService.delete(db, inscrito_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Inscrito com ID {inscrito_id} não encontrado"
        )

    return None