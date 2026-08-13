from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .database import get_db
from .crud import get_all_expenditures, get_by_year, get_by_category
from .crud_extended import (
    get_by_hec,
    get_by_estimate_range,
    get_category_totals,
    get_year_totals
)
from .analytics import calculate_rse_stats, find_anomalies
from .schemas import ExpenditureSchema

# Безпечні імпорти — якщо модуль відсутній, не викликає помилку
try:
    from .aggregations import get_monthly_totals, get_top_categories
except ImportError:
    get_monthly_totals = lambda db: {"error": "aggregations module missing"}
    get_top_categories = lambda db: {"error": "aggregations module missing"}

try:
    from .predictions import simple_linear_prediction
except ImportError:
    simple_linear_prediction = lambda db: {"error": "predictions module missing"}

try:
    from .trends import get_yearly_trend
except ImportError:
    get_yearly_trend = lambda db: {"error": "trends module missing"}

try:
    from .trends_categories import get_category_trends
except ImportError:
    get_category_trends = lambda db: {"error": "trends_categories module missing"}

try:
    from .heatmap import build_heatmap_data
except ImportError:
    build_heatmap_data = lambda db: {"error": "heatmap module missing"}

try:
    from .anomaly_iqr import detect_iqr_anomalies
except ImportError:
    detect_iqr_anomalies = lambda db: {"error": "anomaly_iqr module missing"}

try:
    from .anomaly_mad import detect_mad_anomalies
except ImportError:
    detect_mad_anomalies = lambda db: {"error": "anomaly_mad module missing"}


router = APIRouter()

# ---------------- BASIC CRUD ----------------
@router.get("/expenditures")
def route_all(db: Session = Depends(get_db)):
    data = db.query(Expenditure).all()
    print(f"⚙️ Loaded {len(data)} records")
    return [
        {
            "id": item.id,
            "table": item.table,
            "year": item.year,
            "ms_code": item.ms_code,
            "cat_code": item.cat_code,
            "hec_code": item.hec_code,
            "estimate": item.estimate,
            "rse": item.rse,
            "lower_cib": item.lower_cib,
            "upper_cib": item.upper_cib,
            "flag": item.flag
        }
        for item in data
    ]


@router.get("/expenditures/year/{year}", response_model=list[ExpenditureSchema])
def route_year(year: int, db: Session = Depends(get_db)):
    return get_by_year(db, year)

@router.get("/expenditures/category/{cat}", response_model=list[ExpenditureSchema])
def route_category(cat: str, db: Session = Depends(get_db)):
    return get_by_category(db, cat)

@router.get("/expenditures/hec/{hec}", response_model=list[ExpenditureSchema])
def route_hec(hec: str, db: Session = Depends(get_db)):
    return get_by_hec(db, hec)

@router.get("/expenditures/range/{low}/{high}", response_model=list[ExpenditureSchema])
def route_range(low: float, high: float, db: Session = Depends(get_db)):
    return get_by_estimate_range(db, low, high)

# ---------------- ANALYTICS ----------------
@router.get("/stats/rse")
def route_rse_stats(db: Session = Depends(get_db)):
    return calculate_rse_stats(db)

@router.get("/stats/anomalies")
def route_anomalies(db: Session = Depends(get_db)):
    return find_anomalies(db)

@router.get("/stats/anomalies_iqr")
def route_anomalies_iqr(db: Session = Depends(get_db)):
    return detect_iqr_anomalies(db)

@router.get("/stats/anomalies_mad")
def route_anomalies_mad(db: Session = Depends(get_db)):
    return detect_mad_anomalies(db)

@router.get("/stats/category_totals")
def route_category_totals(db: Session = Depends(get_db)):
    return get_category_totals(db)

@router.get("/stats/year_totals")
def route_year_totals(db: Session = Depends(get_db)):
    return get_year_totals(db)

@router.get("/stats/heatmap")
def route_heatmap(db: Session = Depends(get_db)):
    return build_heatmap_data(db)

@router.get("/stats/category_trends")
def route_category_trends(db: Session = Depends(get_db)):
    return get_category_trends(db)

# ---------------- AGGREGATIONS ----------------
@router.get("/stats/monthly_totals")
def route_monthly_totals(db: Session = Depends(get_db)):
    return get_monthly_totals(db)

@router.get("/stats/top_categories")
def route_top_categories(db: Session = Depends(get_db)):
    return get_top_categories(db)

# ---------------- PREDICTIONS ----------------
@router.get("/stats/prediction")
def route_prediction(db: Session = Depends(get_db)):
    return simple_linear_prediction(db)

# ---------------- TRENDS ----------------
@router.get("/stats/yearly_trend")
def route_yearly_trend(db: Session = Depends(get_db)):
    return get_yearly_trend(db)
