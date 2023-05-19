import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path


app = FastAPI(title='test', version="1.0.0")
app.mount("/static", StaticFiles(directory="static"), name="static")

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "static"))


@app.get('/', response_class=HTMLResponse)
async def testbro(request: Request):
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request},
    )

if __name__ == "__main__":
    uvicorn.run(app, port=8080)