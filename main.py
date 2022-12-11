from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from components.wantedcleanser import WantedCleanser
from components.wantedparser import WantedParser

app = FastAPI()


@app.get("/")
async def root():
    html = WantedParser("https://www.wanted.co.kr").parse()
    WantedCleanser.cleanser(html)
    return HTMLResponse(content=html.__str__(), status_code=200)
