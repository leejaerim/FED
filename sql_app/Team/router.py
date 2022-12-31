from typing import List

from fastapi.routing import APIRouter
from fastapi.param_functions import Depends
from fastapi.requests import Request
from databases.core import Database

from sql_app.Team.models import team
from sql_app.Team.schema import TeamCreate

stack_router = APIRouter()

# Dependency
def get_db_conn(request: Request):
    return request.state.db_conn

@stack_router.post("/team")
async def team_create(
        req: TeamCreate,
        db: Database = Depends(get_db_conn)
):
    query = team.insert()
    values = req.dict()
    await db.execute(query, values)

    return {**req.dict()}