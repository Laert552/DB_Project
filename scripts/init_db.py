# scripts/init_db.py
import sqlite3
DB_NAME = "test.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA journal_mode=WAL;")
    print(f"База данных {DB_NAME} создана.")
    conn.close()

if __name__ == "__main__":
    init_db()