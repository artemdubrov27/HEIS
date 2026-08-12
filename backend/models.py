from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Expenditure(Base):
    __tablename__ = "expenditures"

    id = Column(Integer, primary_key=True, index=True)
    table = Column(String)
    year = Column(Integer)
    ms_code = Column(String)
    cat_code = Column(String)
    hec_code = Column(String)
    estimate = Column(Float)
    rse = Column(Float)
    lower_cib = Column(Float)
    upper_cib = Column(Float)
    flag = Column(String)
