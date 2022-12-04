from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from components.wantedparser import WantedParser

app = FastAPI()


@app.get("/")
async def root():
    html = WantedParser("https://www.wanted.co.kr/api/v4/jobs?1670145066301&country=kr&tag_type_ids=518&job_sort=company.response_rate_order&locations=all&years=-1").parse()
    return HTMLResponse(content=html, status_code=200)
