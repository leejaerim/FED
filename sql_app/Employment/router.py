from databases import Database
from fastapi import APIRouter
from fastapi.param_functions import Depends
from fastapi.requests import Request

from sql_app.Employment.models import emp
from sql_app.Employment.schema import EmpCreate

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