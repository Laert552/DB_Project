# app/crud.py
from sqlalchemy.orm import Session
from .models import MiningPoint, Deposit, Mineral


# CRUD для пунктов
def create_point(db: Session, name: str, staff_count: int, capacity: float):
    point = MiningPoint(name=name, staff_count=staff_count, capacity=capacity)
    db.add(point)
    db.commit()
    db.refresh(point)
    return point

def get_points(db: Session):
    return db.query(MiningPoint).all()

# CRUD для месторождений
def create_deposit(db: Session, point_id: int, extraction_cost: float, annual_output: float, reserves: float, development_method: str):
    deposit = Deposit(point_id=point_id, extraction_cost=extraction_cost, annual_output=annual_output, reserves=reserves, development_method=development_method)
    db.add(deposit)
    db.commit()
    db.refresh(deposit)
    return deposit

def get_deposits(db: Session):
    return db.query(Deposit).all()

# CRUD для полезных ископаемых
def create_mineral(db: Session, deposit_id: int, name: str, unit: str, type: str, market_price: float):
    mineral = Mineral(deposit_id=deposit_id, name=name, unit=unit, type=type, market_price=market_price)
    db.add(mineral)
    db.commit()
    db.refresh(mineral)
    return mineral

def get_minerals(db: Session):
    return db.query(Mineral).all()