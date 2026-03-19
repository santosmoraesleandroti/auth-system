from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import User
from app.utils.security import hash_password, verify_password

# 🔹 Criar usuário (já existe)
def create_user(db: Session, name: str, email: str, password: str):
    hashed_password = hash_password(password)

    user = User(
        name=name,
        email=email,
        password=hashed_password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# 🔹 Buscar usuário por email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


# 🔹 Autenticar usuário (LOGIN)
def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)

    if not user:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Senha inválida")

    return user