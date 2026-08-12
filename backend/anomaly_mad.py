from sqlalchemy.orm import Session
from .models import Expenditure
import numpy as np

def detect_mad_anomalies(db: Session, threshold=3.5):
    data = db.query(Expenditure).all()
    values = np.array([item.estimate for item in data])

    median = np.median(values)
    mad = np.median(np.abs(values - median))

    anomalies = []

    for item in data:
        score = 0.6745 * (item.estimate - median) / mad
        if abs(score) > threshold:
            anomalies.append({
                "cat_code": item.cat_code,
                "hec_code": item.hec_code,
                "estimate": item.estimate,
                "mad_score": score,
                "type": "MAD"
            })

    return anomalies
