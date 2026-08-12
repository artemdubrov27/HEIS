from sqlalchemy.orm import Session
from .models import Expenditure

def get_all_expenditures(db: Session):
    return db.query(Expenditure).all()

def get_by_year(db: Session, year: int):
    return db.query(Expenditure).filter(Expenditure.year == year).all()

def get_by_category(db: Session, cat: str):
    return db.query(Expenditure).filter(Expenditure.cat_code == cat).all()
