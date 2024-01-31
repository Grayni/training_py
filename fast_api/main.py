# pip install fastapi[all]
# pip install uvicorn-browser

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

from reloader import reloader

templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title='New page',
    openapi_url=None,
    docs_url=None,
    redoc_url=None,
)


@app.get("/", status_code=200, response_class=HTMLResponse)
def indexRun(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'reloader': reloader, 'title': 'Main'})


@app.get("/")
async def root():
    return "Hello World"


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        data = await websocket.receive_text()
    except WebSocketDisconnect:
        pass


# uvicorn main:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"
