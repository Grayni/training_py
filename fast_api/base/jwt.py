# uvicorn jwt:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js" --reload-include="main.py"

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates
from models.user import User

templates = Jinja2Templates(directory="templates")

app = FastAPI()
security = HTTPBasic()