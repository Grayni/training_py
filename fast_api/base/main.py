# pip install fastapi[all]

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from models.User import User

templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title='docs',
    # openapi_url=None,
    # docs_url=None,
    redoc_url=None
)

app.mount('/static', StaticFiles(directory='static'), name='static')


# Models
user_1: User = User(id=1, name='John Doe', age=32)


@app.get('/users')
def showUser():
    return user_1.model_dump()  # dict()


# @app.post("/user")
# async def show_user(usr: User):
#     return {"name": usr.name,
#             "age": usr.age,
#             "is_adult": usr.age >= 18}


@app.get('/user', response_class=HTMLResponse)
def userFields(request: Request):
    return templates.TemplateResponse('user.html', {'request': request, 'title': 'User'})


@app.post('/user')
def ageUser(name: str = Form(...), age: int = Form(ge=0, lt=111)):
    return {'name': name, 'age': age, 'is_adult': age >= 18}


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


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        data = await websocket.receive_text()
    except WebSocketDisconnect:
        pass


# uvicorn main:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"
