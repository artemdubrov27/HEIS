from sqlalchemy.orm import Session
from sqlalchemy import func
from .models import Expenditure
import pandas as pd

def build_heatmap_data(db: Session):
    data = db.query(
        Expenditure.year,
        Expenditure.cat_code,
        Expenditure.estimate
    ).all()

    df = pd.DataFrame(data, columns=["year", "cat", "estimate"])
    pivot = df.pivot_table(values="estimate", index="cat", columns="year", aggfunc="sum")
    corr = pivot.corr()

    return corr.to_dict()
