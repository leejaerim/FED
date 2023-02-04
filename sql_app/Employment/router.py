from typing import List

from databases import Database
from fastapi import APIRouter
from fastapi.param_functions import Depends
from fastapi.requests import Request

from sql_app.Employment.models import emp
from sql_app.Employment.schema import EmpCreate, EmpSelect

emp_router = APIRouter()

# Dependency
def get_db_conn(request: Request):
    return request.state.db_conn


@emp_router.get("/api/v1/emp",response_model=dict)
@emp_router.get("/api/v1/emp/{page}",response_model=dict)
async def emp_select(
        page : int = 1,
        limit : int = 20,
        db : Database = Depends(get_db_conn)
):
    offset = (page-1)*limit
    query = emp.select().offset(offset).limit(limit)
    emp_result = {}
    emp_result['total'] = len(await db.fetch_all(emp.select()))
    emp_result['row'] = await db.fetch_all(query)
    return emp_result


@emp_router.get("/api/v1/emp/id/{id}",response_model=EmpSelect)
async def emp_select(
        id : int,
        db : Database = Depends(get_db_conn)
):
    query = emp.select().where(emp.columns.emp_id == id)
    return await db.fetch_one(query)