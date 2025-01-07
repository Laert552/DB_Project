# app/models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MiningPoint(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    staff_count = Column(Integer)
    capacity = Column(Float)

    deposits = relationship("Deposit", back_populates="point")

class Deposit(Base):
    __tablename__ = "deposits"
    id = Column(Integer, primary_key=True, index=True)
    extraction_cost = Column(Float)
    annual_output = Column(Float)
    reserves = Column(Float)
    development_method = Column(String)
    point_id = Column(Integer, ForeignKey("points.id"))

    point = relationship("MiningPoint", back_populates="deposits")
    minerals = relationship("Mineral", back_populates="deposit")

class Mineral(Base):
    __tablename__ = "minerals"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    type = Column(String)
    market_price = Column(Float)
    deposit_id = Column(Integer, ForeignKey("deposits.id"))

    deposit = relationship("Deposit", back_populates="minerals")