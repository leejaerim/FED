from typing import List

from databases import Database
from fastapi import APIRouter
from fastapi.param_functions import Depends
from fastapi.requests import Request
from sqlalchemy import select
from sql_app.Company.models import company
from sql_app.Company.schema import CompanySelect
from sql_app.Employment.models import emp_stack
from sql_app.Stack.models import stack
from sql_app.Stack.schema import StackSelect

company_router = APIRouter()


# Dependency
def get_db_conn(request: Request):
    return request.state.db_conn


@company_router.get("/api/v1/company", response_model=List[CompanySelect])
@company_router.get("/api/v1/company/{page}", response_model=List[CompanySelect])
async def company_select(
        page: int = 1,
        limit: int = 20,
        db: Database = Depends(get_db_conn)
):
    offset = (page - 1) * limit
    query = company.select().offset(offset).limit(limit).group_by(company.columns.company_id)
    return await db.fetch_all(query)


@company_router.get("/api/v1/company/id/{id}", response_model=CompanySelect)
async def company_select(
        id: int,
        db: Database = Depends(get_db_conn)
):
    query = company.select().where(company.columns.company_id == id)
    return await db.fetch_one(query)

@company_router.get("/api/v1/company/id/{id}/stack", response_model=List[StackSelect])
async def company_select(
        id: int,
        db: Database = Depends(get_db_conn)
):
    query = select([emp_stack, company, stack]).where(company.columns.company_id == id).where(
        emp_stack.columns.emp_fk == company.columns.emp_fk).where(stack.columns.stack_id == emp_stack.columns.stack_fk).group_by(stack.columns.stack_id)
    return await db.fetch_all(query)
