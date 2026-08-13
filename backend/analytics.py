from sqlalchemy.orm import Session
from .models import Expenditure


def calculate_rse_stats(db: Session):
    # Отримуємо всі записи
    data = db.query(Expenditure).all()

    # Беремо лише ті значення RSE, які не None
    rse_values = [item.rse for item in data if item.rse is not None]

    # Якщо список порожній — повертаємо нулі
    if not rse_values:
        return {
            "average_rse": 0,
            "max_rse": 0,
            "min_rse": 0
        }

    avg_rse = sum(rse_values) / len(rse_values)
    max_rse = max(rse_values)
    min_rse = min(rse_values)

    return {
        "average_rse": avg_rse,
        "max_rse": max_rse,
        "min_rse": min_rse
    }


def find_anomalies(db: Session):
    # Отримуємо всі записи
    data = db.query(Expenditure).all()

    anomalies = []

    for item in data:
        # Перевіряємо, чи є флаг і чи він не порожній
        if item.flag and str(item.flag).strip() != "":
            anomalies.append({
                "cat_code": item.cat_code,
                "hec_code": item.hec_code,
                "estimate": item.estimate,
                "flag": item.flag
            })

    return anomalies
