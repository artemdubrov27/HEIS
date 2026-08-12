from pydantic import BaseModel

class ExpenditureSchema(BaseModel):
    id: int
    table: str
    year: int
    ms_code: str
    cat_code: str
    hec_code: str
    estimate: float
    rse: float
    lower_cib: float
    upper_cib: float
    flag: str

    class Config:
        orm_mode = True
