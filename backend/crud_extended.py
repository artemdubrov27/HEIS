from sqlalchemy.orm import Session
from sqlalchemy import func
from .models import Expenditure

def get_by_hec(db: Session, hec_code: str):
    return db.query(Expenditure).filter(Expenditure.hec_code == hec_code).all()

def get_by_estimate_range(db: Session, low: float, high: float):
    return db.query(Expenditure).filter(
        Expenditure.estimate >= low,
        Expenditure.estimate <= high
    ).all()

def get_category_totals(db: Session):
    results = db.query(
        Expenditure.cat_code,
        func.sum(Expenditure.estimate).label("total")
    ).group_by(Expenditure.cat_code).all()

    return [{"cat_code": r[0], "total": r[1]} for r in results]

def get_year_totals(db: Session):
    results = db.query(
        Expenditure.year,
        func.sum(Expenditure.estimate).label("total")
    ).group_by(Expenditure.year).all()

    return [{"year": r[0], "total": r[1]} for r in results]
