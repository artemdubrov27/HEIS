import pandas as pd
from sqlalchemy.orm import Session
from .models import Expenditure

def load_csv_to_db(db: Session, csv_path: str):
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        exp = Expenditure(
            table=row["Table"],
            year=row["Year"],
            ms_code=row["MsCode"],
            cat_code=row["CatCode"],
            hec_code=row["HECCode"],
            estimate=float(str(row["Estimate"]).strip()),
            rse=float(str(row["RSE"]).strip()),
            lower_cib=float(str(row["LowerCIB"]).strip()),
            upper_cib=float(str(row["UpperCIB"]).strip()),
            flag=row["Flag"]
        )
        db.add(exp)

    db.commit()
