from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from gateways.database import get_db
from schemas.user_schemas import UserCreate, UserResponse
from services.user_service import get_users, get_user, create_user, update_user, delete_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/{id}", response_model=UserResponse)
def read_user(id: int, db: Session = Depends(get_db)):
    return get_user(db, id)

@router.post("/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.put("/{id}", response_model=UserResponse)
def update_existing_user(id: int, user: UserCreate, db: Session = Depends(get_db)):
    updated_user = update_user(db, id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return updated_user

@router.delete("/{id}")
def delete_existing_user(id: int, db: Session = Depends(get_db)):
    deleted = delete_user(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Usuário deletado com sucesso"}
