from sqlalchemy.orm import Session
from sqlalchemy import func
from .models import Expenditure

def get_yearly_trend(db: Session):
    results = db.query(
        Expenditure.year,
        func.sum(Expenditure.estimate).label("total")
    ).group_by(
        Expenditure.year
    ).order_by(
        Expenditure.year
    ).all()

    return [{"year": r[0], "total": r[1]} for r in results]
