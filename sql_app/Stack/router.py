from typing import List
from fastapi.routing import APIRouter
from sql_app.Stack.schema import StackCreate, StackSelect
from fastapi.param_functions import Depends
from sql_app.Stack.models import stack
from fastapi.requests import Request
from databases.core import Database
stack_router = APIRouter()

# Dependency
def get_db_conn(request: Request):
    return request.state.db_conn

@stack_router.get("/stack",response_model=List[StackSelect])
@stack_router.get("/stack/{page}",response_model=List[StackSelect])
async def stack_select(
        page : int = 1,
        limit : int = 10,
        db : Database = Depends(get_db_conn)
):
    offset = (page-1)*limit
    query = stack.select().offset(offset).limit(limit)
    return await db.fetch_all(query)

@stack_router.post("/stack")
async def stack_create(
        req: StackCreate,
        db: Database = Depends(get_db_conn)
):
    query = stack.insert()
    values = req.dict()
    await db.execute(query, values)
    return {**req.dict()}

@stack_router.get("/stack/id/{id}",response_model=StackSelect)
async def stack_select(
        id : int,
        db : Database = Depends(get_db_conn)
):
    query = stack.select().where(stack.columns.stack_id == id)
    return await db.fetch_one(query)

@stack_router.delete("/stack/{id}")
async def stack_delete(
    id: int,
    db: Database = Depends(get_db_conn)
):
    query = stack.delete().where(stack.columns.stack_id == id)
    await db.execute(query)
    return {"result": "success"}