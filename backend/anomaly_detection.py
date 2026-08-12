from sqlalchemy.orm import Session
from statistics import mean, stdev
from .models import Expenditure

def detect_zscore_anomalies(db: Session, threshold: float = 3.0):
    data = db.query(Expenditure).all()
    values = [item.estimate for item in data]

    avg = mean(values)
    sd = stdev(values)

    anomalies = []

    for item in data:
        z = (item.estimate - avg) / sd
        if abs(z) >= threshold:
            anomalies.append({
                "cat_code": item.cat_code,
                "hec_code": item.hec_code,
                "estimate": item.estimate,
                "zscore": z
            })

    return anomalies
