from sqlalchemy.orm import Session
fom app.database import SessionLocal, engine
from app.models import Base, MiningPoint, Deposit, Mineral

# Создание таблиц, если их нет
Base.metadata.create_all(bind=engine)

def populate_data():
    db: Session = SessionLocal()

    try:
        # Добавление пунктов
        point1 = MiningPoint(name="Пункт А", staff_count=50, capacity=1000.0)
        point2 = MiningPoint(name="Пункт Б", staff_count=30, capacity=750.0)
        db.add_all([point1, point2])
        db.commit()

        # Добавление месторождений
        deposit1 = Deposit(
            extraction_cost=500.75,
            annual_output=20000.0,
            reserves=100000.0,
            development_method="Карьерный способ",
            point_id=point1.id,
        )
        deposit2 = Deposit(
            extraction_cost=300.50,
            annual_output=15000.0,
            reserves=50000.0,
            development_method="Подземный способ",
            point_id=point2.id,
        )
        db.add_all([deposit1, deposit2])
        db.commit()

        # Добавление полезных ископаемых
        mineral1 = Mineral(
            name="Золото",
            unit="кг",
            type="Драгоценный металл",
            market_price=50000.0,
            deposit_id=deposit1.id,
        )
        mineral2 = Mineral(
            name="Железо",
            unit="т",
            type="Металл",
            market_price=250.0,
            deposit_id=deposit2.id,
        )
        db.add_all([mineral1, mineral2])
        db.commit()

        print("База данных успешно заполнена начальными значениями.")
    except Exception as e:
        print(f"Ошибка при заполнении базы данных: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    populate_data()