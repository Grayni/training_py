# pip install fastapi[all]

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, Form, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from models.models import User, Feedback, UserCreate
from pydantic import ValidationError

templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title='docs',
    # openapi_url=None,
    # docs_url=None,
    redoc_url=None
)

app.mount('/static', StaticFiles(directory='static'), name='static')


# Models
user: User = User(id=1, name='John Doe', age=32)


@app.get('/users')
def showUser():
    return user.model_dump()  # dict()


@app.get('/user', response_class=HTMLResponse)
def userFields(request: Request):
    return templates.TemplateResponse('user.html', {'request': request, 'title': 'User'})


@app.post('/user')
def ageUser(name: str = Form(...), age: int = Form(ge=0, lt=111)):
    return {'name': name, 'age': age, 'is_adult': age >= 18}


fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"}
}


@app.get('/users/{user_id}')
def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {'error': 'User not found'}


feedbacks = []


@app.post('/feedback')
async def send_feedback(feedback: Feedback):
    feedbacks.append({'name': feedback.name, 'message': feedback.message})
    return {'message': f'Feedback received. Thank you, {feedback.name}'}


@app.get('/feedback')
async def show_feedback():
    return feedbacks


@app.get('/', status_code=200, response_class=HTMLResponse)
def indexRun(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'title': 'Main'})


@app.get('/hello')
async def root():
    return "Hello World"


@app.get('/response', response_class=FileResponse)
def responseRun():
    return 'response.html'


@app.get('/calculate', response_class=HTMLResponse)
def calculate(request: Request):
    return templates.TemplateResponse('calculate.html', {'request': request, 'title': 'Calculate'})


@app.post('/calculate')
def calculate(num1: int = Form(ge=0, lt=111), num2: int = Form(ge=0, lt=111)):
    print(f'num1={num1}; num2={num2}')
    return f'Result: {num1 + num2}'


@app.get('/custom')
def read_custom_message():
    return {'message': 'This is a custom message!'}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"},
                 {"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"},
                 {"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"},
                 {"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/fake-items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


users: list[UserCreate] = []


@app.post("/create-user")
async def create_user(new_user: UserCreate):
    users.append(new_user)
    return new_user


@app.get("/showuser")
async def show_users():
    return {"users": users}


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        data = await websocket.receive_text()
    except WebSocketDisconnect:
        pass


# uvicorn main:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"
