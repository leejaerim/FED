from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    html = """
        <HTML>
        <BODY>
            <H1> HI HELLO WORLD </H1>
        </BODY>
        </HTML>
    """
    return HTMLResponse(content=html, status_code=200)