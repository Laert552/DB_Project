# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL подключения к базе данных
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)