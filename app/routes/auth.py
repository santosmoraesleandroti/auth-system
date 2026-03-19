from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import UserCreate
from app.services.auth_service import create_user, authenticate_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔹 Rota de cadastro
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(db, user.name, user.email, user.password)

    return {
        "message": "Usuário criado com sucesso",
        "email": new_user.email
    }


# 🔹 Rota de login
@router.post("/login")
def login(user: dict, db: Session = Depends(get_db)):
    email = user.get("email")
    password = user.get("password")

    logged_user = authenticate_user(db, email, password)

    return {
        "message": "Login realizado com sucesso",
        "email": logged_user.email
    }