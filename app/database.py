from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# conexão com MySQL (senha com @ precisa ser codificada como %40)
DATABASE_URL = "mysql+pymysql://root:%40Zed202250@localhost/auth_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()