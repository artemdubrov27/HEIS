from sqlalchemy.orm import Session
from sqlalchemy import func
from .models import Expenditure

def get_monthly_totals(db: Session):
    return db.query(
        Expenditure.year,
        Expenditure.cat_code,
        func.sum(Expenditure.estimate).label("total")
    ).group_by(
        Expenditure.year,
        Expenditure.cat_code
    ).all()

def get_top_categories(db: Session, limit: int = 10):
    return db.query(
        Expenditure.cat_code,
        func.sum(Expenditure.estimate).label("total")
    ).group_by(
        Expenditure.cat_code
    ).order_by(
        func.sum(Expenditure.estimate).desc()
    ).limit(limit).all()
