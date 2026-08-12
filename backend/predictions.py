from sqlalchemy.orm import Session
from sqlalchemy import func
from .models import Expenditure

def simple_linear_prediction(db: Session):
    results = db.query(
        Expenditure.year,
        func.sum(Expenditure.estimate).label("total")
    ).group_by(
        Expenditure.year
    ).order_by(
        Expenditure.year
    ).all()

    years = [r[0] for r in results]
    totals = [r[1] for r in results]

    if len(years) < 2:
        return {"error": "Not enough data"}

    slope = (totals[-1] - totals[0]) / (years[-1] - years[0])
    next_year = years[-1] + 1
    prediction = totals[-1] + slope

    return {
        "next_year": next_year,
        "prediction": prediction
    }
