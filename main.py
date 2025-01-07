from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base
from app.crud import create_point, get_points, create_deposit, get_deposits, create_mineral, get_minerals
from scripts import init_db
from app.populate_db import populate_data

# Создание таблицw
Base.metadata.create_all(bind=engine)
init_db()
populate_data()
app = FastAPI()

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршруты для пунктов
@app.post("/points/")
def create_point_route(name: str, staff_count: int, capacity: float, db: Session = Depends(get_db)):
    return create_point(db, name, staff_count, capacity)

@app.get("/points/")
def read_points(db: Session = Depends(get_db)):
    return get_points(db)

# Маршруты для месторождений
@app.post("/deposits/")
def create_deposit_route(point_id: int, extraction_cost: float, annual_output: float, reserves: float, development_method: str, db: Session = Depends(get_db)):
    return create_deposit(db, point_id, extraction_cost, annual_output, reserves, development_method)

@app.get("/deposits/")
def read_deposits(db: Session = Depends(get_db)):
    return get_deposits(db)

# Маршруты для полезных ископаемых
@app.post("/minerals/")
def create_mineral_route(deposit_id: int, name: str, unit: str, type: str, market_price: float, db: Session = Depends(get_db)):
    return create_mineral(db, deposit_id, name, unit, type, market_price)

@app.get("/minerals/")
def read_minerals(db: Session = Depends(get_db)):
    return get_minerals(db)