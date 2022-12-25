from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from components.wantedcleanser import WantedCleanser
from components.wantedparser import WantedParser

app = FastAPI()


@app.get("/")
async def root():
    html = WantedParser("https://www.wanted.co.kr").parse()
    WantedCleanser(html).cleanser()
    return HTMLResponse(content=html.__str__(), status_code=200)


@app.get("/parse/jobs/{jobs_id}")
async def get_data(jobs_id):
    data_dict = WantedParser("https://www.wanted.co.kr").get_info_of(jobs_id)
    return HTMLResponse(content=data_dict.__str__(), status_code=200)


@app.get("/parse/jobs/{jobs_id}/stack")
async def get_stack_data(jobs_id):
    data_dict = WantedParser("https://www.wanted.co.kr").get_info_of(jobs_id)
    cleanser = WantedCleanser(data_dict)
    return HTMLResponse(content=cleanser.get_stack().__str__(), status_code=200)