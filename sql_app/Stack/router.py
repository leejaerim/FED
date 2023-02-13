from typing import List
from fastapi.routing import APIRouter
from sqlalchemy import select

from sql_app.Company.models import company
from sql_app.Company.schema import CompanySelect
from sql_app.Employment.models import emp_stack
from sql_app.Stack.schema import StackCreate, StackSelect
from fastapi.param_functions import Depends
from sql_app.Stack.models import stack
from fastapi.requests import Request
from databases.core import Database
stack_router = APIRouter()

# Dependency
def get_db_conn(request: Request):
    return request.state.db_conn

@stack_router.get("/api/v1/stack",response_model=List[StackSelect])
@stack_router.get("/api/v1/stack/{page}",response_model=List[StackSelect])
async def stack_select(
        page : int = 1,
        limit : int = 10,
        db : Database = Depends(get_db_conn)
):
    offset = (page-1)*limit
    query = stack.select().offset(offset).limit(limit)
    return await db.fetch_all(query)

@stack_router.post("/api/v1/stack")
async def stack_create(
        req: StackCreate,
        db: Database = Depends(get_db_conn)
):
    query = stack.insert()
    values = req.dict()
    await db.execute(query, values)
    return {**req.dict()}

@stack_router.get("/api/v1/stack/id/{id}",response_model=List[StackSelect])
async def stack_select(
        id : int,
        db : Database = Depends(get_db_conn)
):
    query = stack.select().where(stack.columns.stack_id == id)
    #query = emp_stack.select().where(emp_stack.columns.stack_fk == id)
    return await db.fetch_all(query)

@stack_router.get("/api/v1/stack/id/{id}/company",response_model=List[CompanySelect])
async def stack_select(
        id : int,
        db : Database = Depends(get_db_conn)
):
    query = select([emp_stack, company]).where(emp_stack.columns.stack_fk == id).where(emp_stack.columns.emp_fk == company.columns.emp_fk).group_by(company.columns.company_id)
    #query = emp_stack.select().where(emp_stack.columns.stack_fk == id)
    return await db.fetch_all(query)

@stack_router.delete("/api/v1/stack/{id}")
async def stack_delete(
    id: int,
    db: Database = Depends(get_db_conn)
):
    query = stack.delete().where(stack.columns.stack_id == id)
    await db.execute(query)
    return {"result": "success"}