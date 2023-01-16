from datetime import datetime

from pydantic import BaseModel


class CompanySelect(BaseModel):
    company_id: int
    company_name: str
    logo: str
    location: str
    country: str
    emp_fk: int
