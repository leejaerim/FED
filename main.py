from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from components.wantedparser import WantedParser

app = FastAPI()


@app.get("/")
async def root():

    html = WantedParser("https://www.wanted.co.kr/wd/138471").parse()
    return HTMLResponse(content=html, status_code=200)
