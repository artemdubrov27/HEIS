from sqlalchemy.orm import Session
from .models import Expenditure

def calculate_rse_stats(db: Session):
    data = db.query(Expenditure).all()

    # Беремо лише ті значення, які не None
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
