# pip install fastapi[all]
# uvicorn main:app2 --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"

from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Depends, status, HTTPException, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials

templates = Jinja2Templates(directory="templates")

app2 = FastAPI(
    title='docs',
    # openapi_url=None,
    # docs_url=None,
    redoc_url=None
)
#security = HTTPBasic()


@app2.get('/')
async def auth():
    return {'message': 'good'}


@app2.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        data = await websocket.receive_text()
    except WebSocketDisconnect:
        pass
