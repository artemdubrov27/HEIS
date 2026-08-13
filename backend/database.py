import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../data/heis.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    Base.metadata.create_all(bind=engine)


def init_db_from_csv():
    from .models import Expenditure   # <— імпорт всередині функції, не на рівні модуля

    db: Session = SessionLocal()

    if db.query(Expenditure).count() == 0:
        print("⚠ База порожня — завантажую CSV...")

        csv_path = os.path.join(BASE_DIR, "../data/exp-t1to4-datafile_2023.csv")

        if not os.path.exists(csv_path):
            print(f"❌ CSV файл не знайдено: {csv_path}")
            return

        df = pd.read_csv(csv_path)

        for _, row in df.iterrows():
            exp = Expenditure(
                table=row.get("Table"),
                year=row.get("Year"),
                ms_code=row.get("MsCode"),
                cat_code=row.get("CatCode"),
                hec_code=row.get("HECCode"),
                estimate=float(str(row.get("Estimate")).strip()),
                rse=float(str(row.get("RSE")).strip()),
                lower_cib=float(str(row.get("LowerCIB")).strip()),
                upper_cib=float(str(row.get("UpperCIB")).strip()),
                flag=row.get("Flag")
            )
            db.add(exp)

        db.commit()
        print("✅ База успішно заповнена з CSV.")
