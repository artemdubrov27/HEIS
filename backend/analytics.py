from sqlalchemy.orm import Session
from .models import Expenditure

def calculate_rse_stats(db: Session):
    data = db.query(Expenditure).all()

    rse_values = [item.rse for item in data]
    avg_rse = sum(rse_values) / len(rse_values)

    max_rse = max(rse_values)
    min_rse = min(rse_values)

    return {
        "average_rse": avg_rse,
        "max_rse": max_rse,
        "min_rse": min_rse
    }

def find_anomalies(db: Session):
    data = db.query(Expenditure).all()

    anomalies = []

    for item in data:
        if item.flag and item.flag.strip() != "":
            anomalies.append({
                "cat_code": item.cat_code,
                "hec_code": item.hec_code,
                "estimate": item.estimate,
                "flag": item.flag
            })

    return anomalies
