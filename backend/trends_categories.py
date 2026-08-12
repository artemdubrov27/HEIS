from sqlalchemy.orm import Session
from sqlalchemy import func
from .models import Expenditure

def get_category_trends(db: Session):
    results = db.query(
        Expenditure.cat_code,
        Expenditure.year,
        func.sum(Expenditure.estimate).label("total")
    ).group_by(
        Expenditure.cat_code,
        Expenditure.year
    ).order_by(
        Expenditure.cat_code,
        Expenditure.year
    ).all()

    trends = {}
    for cat, year, total in results:
        if cat not in trends:
            trends[cat] = []
        trends[cat].append({"year": year, "total": total})

    return trends
