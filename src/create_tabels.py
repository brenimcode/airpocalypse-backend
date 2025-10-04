from typing import Generator

from core.db import SessionLocal, init_db

if __name__ == "__main__":
    init_db()
    print("Tabelas criadas com sucesso!")


    def get_db() -> Generator:
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
