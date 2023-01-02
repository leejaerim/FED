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



@emp_router.post("/emp/")
async def emp_create(
        req: EmpCreate,
        db: Database = Depends(get_db_conn)
):
    query = emp.insert()
    values = req.dict()
    await db.execute(query, values)

    return {**req.dict()}

@emp_router.get("/emp",response_model=List[EmpSelect])
@emp_router.get("/emp/{page}",response_model=List[EmpSelect])
async def stack_select(
        page : int = 1,
        limit : int = 10,
        db : Database = Depends(get_db_conn)
):
    offset = (page-1)*limit
    query = emp.select().offset(offset).limit(limit)
    return await db.fetch_all(query)


@emp_router.get("/emp/id/{id}",response_model=EmpSelect)
async def stack_select(
        id : int,
        db : Database = Depends(get_db_conn)
):
    query = emp.select().where(emp.columns.emp_id == id)
    return await db.fetch_one(query)

@emp_router.delete("/emp/{id}")
async def stack_delete(
    id: int,
    db: Database = Depends(get_db_conn)
):
    query = emp.delete().where(emp.columns.emp_id == id)
    await db.execute(query)
    return {"result": "success"}