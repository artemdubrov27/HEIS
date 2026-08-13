from pydantic import BaseModel

class ExpenditureSchema(BaseModel):
    id: int | None = None
    table: str | None = None
    year: str | None = None
    ms_code: str | None = None
    cat_code: str | None = None
    hec_code: str | None = None
    estimate: float | None = None
    rse: float | None = None
    lower_cib: float | None = None
    upper_cib: float | None = None
    flag: str | None = None

    class Config:
        from_attributes = True  # New sintacsys for Pydantic v2
