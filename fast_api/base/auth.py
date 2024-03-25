# uvicorn auth:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js" --reload-include="main.py"

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates
from models.user import User

templates = Jinja2Templates(directory="templates")

app = FastAPI()
security = HTTPBasic()

# database simulation
USER_DATA = [User(**{"username": "user1", "password": "pass1"}), User(**{"username": "user2", "password": "pass2"})]


def get_user_from_db(username: str):
    for user in USER_DATA:
        if user.username == username:
            return user
    return None


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_user_from_db(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user


@app.get('/')
def main():
    return {'message': 'Hello World!!'}


@app.get('/protected_resource')
def get_protected_resource(user: User = Depends(authenticate_user)):
    return {"message": "You have access to the protected resource!", "user_info": user}


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        data = await websocket.receive_text()
    except WebSocketDisconnect:
        pass




