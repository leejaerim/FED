from typing import List

from fastapi.routing import APIRouter
from fastapi.param_functions import Depends
from fastapi.requests import Request
from databases.core import Database

from sql_app.Team.models import team
from sql_app.Team.schema import TeamCreate, TeamSelect

team_router = APIRouter()

# Dependency
def get_db_conn(request: Request):
    return request.state.db_conn

@team_router.post("/team")
async def team_create(
        req: TeamCreate,
        db: Database = Depends(get_db_conn)
):
    query = team.insert()
    values = req.dict()
    await db.execute(query, values)

    return {**req.dict()}


@team_router.get("/team",response_model=List[TeamSelect])
@team_router.get("/team/{page}",response_model=List[TeamSelect])
async def team_select(
        page : int = 1,
        limit : int = 10,
        db : Database = Depends(get_db_conn)
):
    offset = (page-1)*limit
    query = team.select().offset(offset).limit(limit)
    return await db.fetch_all(query)



@team_router.get("/team/id/{id}",response_model=TeamSelect)
async def stack_select(
        id : int,
        db : Database = Depends(get_db_conn)
):
    query = team.select().where(team.columns.team_id == id)
    return await db.fetch_one(query)

@team_router.delete("/team/{id}")
async def stack_delete(
    id: int,
    db: Database = Depends(get_db_conn)
):
    query = team.delete().where(team.columns.team_id == id)
    await db.execute(query)
    return {"result": "success"}