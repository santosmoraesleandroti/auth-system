from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routes import auth

app = FastAPI()

# cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "API funcionando"}