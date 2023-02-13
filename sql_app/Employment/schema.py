from datetime import datetime

from pydantic import BaseModel

class EmpCreate(BaseModel):
    emp_title : str
    register_date : datetime
    dead_line : datetime
    creer : int
    company_fk : int

class EmpSelect(BaseModel):
    emp_id : int
    emp_title: str
    register_date: datetime
    dead_line: datetime
    creer: int

class EmpStackSelect(BaseModel):
    emp_fk : int
    stack_fk : int