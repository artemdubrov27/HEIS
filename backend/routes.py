from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .database import get_db
from .crud import get_all_expenditures, get_by_year, get_by_category
from .crud_extended import get_by_hec, get_by_estimate_range, get_category_totals, get_year_totals
from .analytics import calculate_rse_stats, find_anomalies
from .aggregations import get_monthly_totals, get_top_categories
from .predictions import simple_linear_prediction
from .trends import get_yearly_trend
from .trends_categories import get_category_trends
from .heatmap import build_heatmap_data
from .anomaly_iqr import detect_iqr_anomalies
from .anomaly_mad import detect_mad_anomalies
from .schemas import ExpenditureSchema

router = APIRouter()

# ---------------- BASIC CRUD ----------------
@router.get("/expenditures", response_model=list[ExpenditureSchema])
def route_all(db: Session = Depends(get_db)):
    return get_all_expenditures(db)

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
