from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from components.cleanserImpl import WantedCleanser
from components.parserImpl import WantedParser
from components.savers import Savers
from saver.companysaver import CompanySaver
from saver.jobsaver import JobSaver
from sql_app.Company.router import company_router
from sql_app.Employment.router import emp_router
from sql_app.Stack.router import stack_router
from sql_app.Team.router import team_router
from sql_app.database import db_instance
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return HTMLResponse(content="{code:200}", status_code=200)

@app.get("/api/v1/async")
async def async_data():
    parser_dict = WantedParser("https://www.wanted.co.kr").parse()
    cleansed_list = WantedCleanser(parser_dict).cleanser()
    savers = Savers()
    savers.add(JobSaver(cleansed_list))
    savers.add(CompanySaver(cleansed_list))
    savers.save()
    return HTMLResponse(content=cleansed_list.__str__(), status_code=200)


@app.get("/parse/jobs/{jobs_id}")
async def get_data(jobs_id):
    data_dict = WantedParser("https://www.wanted.co.kr").get_info_of(jobs_id)
    return HTMLResponse(content=data_dict.__str__(), status_code=200)


@app.get("/parse/jobs/{jobs_id}/stack")
async def get_stack_data(jobs_id):
    data_dict = WantedParser("https://www.wanted.co.kr").get_info_of(jobs_id)
    cleanser = WantedCleanser(data_dict)
    return HTMLResponse(content=cleanser.get_stack().__str__(), status_code=200)


# 서버 시작시 db connect
@app.on_event("startup")
async def startup():
    await db_instance.connect()

# 서버 종료시 db disconnect
@app.on_event("shutdown")
async def shutdown():
    await db_instance.disconnect()

# fastapi middleware, request state 에 db connection 심기
@app.middleware("http")
async def state_insert(request: Request, call_next):
    request.state.db_conn = db_instance
    response = await call_next(request)
    return response

app.include_router(stack_router)
app.include_router(emp_router)
app.include_router(team_router)
app.include_router(company_router)