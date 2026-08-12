from sqlalchemy.orm import Session
from .models import Expenditure
import numpy as np

def detect_iqr_anomalies(db: Session):
    data = db.query(Expenditure).all()
    values = np.array([item.estimate for item in data])

    q1 = np.percentile(values, 25)
    q3 = np.percentile(values, 75)
    iqr = q3 - q1

    low = q1 - 1.5 * iqr
    high = q3 + 1.5 * iqr

    anomalies = []

    for item in data:
        if item.estimate < low or item.estimate > high:
            anomalies.append({
                "cat_code": item.cat_code,
                "hec_code": item.hec_code,
                "estimate": item.estimate,
                "type": "IQR"
            })

    return anomalies
