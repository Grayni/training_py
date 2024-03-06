# pip install fastapi[all]
# uvicorn main:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"
import re
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, Form, Body, Cookie, Response, Header, HTTPException
from typing import Annotated
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

from models.models import User, Feedback, UserCreate, UserAuth

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


@app.get('/cookie')
def cookie(response: Response):
    now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    response.set_cookie(key='last_visit', value=now)
    return {"message": "cookies set", "last visit": now}


sample_user: dict = {"username": "user123", "password": "password123"}
fake_db: list[UserAuth] = [UserAuth(**sample_user)]
sessions: dict = {}


@app.get('/items/')
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}


X_Tokens = ['foo', 'bar']


@app.get('/x_token')
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}


@app.get('/get_user_agent')
async def user_agent(user_agent: str = Header()):
    return {'User-Agent': user_agent}


@app.get('/response_user_agent')
async def resp_user_agent():
    data = 'hello from here'
    return Response(content=data, media_type='text/plain', headers={'Secret-Code': '12345'})


@app.get('/new_user_agent')
async def new_user_agent(response: Response):
    response.headers['Secret-Code'] = '123456'
    return {'message': 'Hello from my api'}


@app.get('/headers')
async def headers(user_agent: Annotated[str | None, Header()]):
    data = 'new headers'
    return Response(content=data, media_type='text/plain', headers={
        'User-Agent': user_agent, 'Accept-Language': 'en-US,en;q=0.9,es;q=0.8'})


def check_headers(headers: Request.headers):
    if "User-Agent" not in headers:
        raise HTTPException(status_code=400, detail="The User-Agent header not found!")

    if "Accept-Language" not in headers:
        raise HTTPException(status_code=400, detail="The Accept-Language header not found!")

    pattern = r"(?i:(?:\*|[a-z\-]{2,5})(?:;q=\d\.\d)?,)+(?:\*|[a-z\-]{2,5})(?:;q=\d\.\d)?"
    if not re.fullmatch(pattern, headers["Accept-Language"]):
        raise HTTPException(
            status_code=400,
            detail="The Accept-Language header is not in the correct format"
        )


@app.get("/headers2")
async def get_headers(request: Request) -> dict:
    check_headers(request.headers)
    return {
        "User-Agent": request.headers["user-agent"],
        "Accept-Language": request.headers["accept-language"]
    }

@app.post('/login')
def login(response: Response, user: UserAuth):
    for person in fake_db:
        if person.username == user.username and person.password == user.password:
            session_token = 'abc1234'
            sessions[session_token] = user

            response.set_cookie(key='session_token', value=session_token, httponly=True)
            return {'message': 'cookies set'}
    return {'message': 'invalid username or password'}


@app.get('/user')
async def user_info(session_token=Cookie()):
    user = sessions.get(session_token)

    if user:
        return user.dict()
    return {'message': 'invalid session token'}


@app.post('/logout', status_code=204)
async def logout_user(response: Response):
    response.delete_cookie('example_access_token')

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
async def send_feedback(feedback: Feedback = Body(..., description="test feedback")):
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


@app.get('/fake-items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


users: list[UserCreate] = []


@app.post('/create-user')
async def create_user(new_user: UserCreate):
    print(new_user)
    users.append(new_user)
    return new_user


@app.get('/showuser')
async def show_users():
    return {"users": users}


sample_products = [{"product_id": 123, "name": "Smartphone", "category": "Electronics", "price": 599.99},
                   {"product_id": 456, "name": "Phone Case", "category": "Accessories", "price": 19.99},
                   {"product_id": 789, "name": "Iphone", "category": "Electronics", "price": 1299.99},
                   {"product_id": 101, "name": "Headphones", "category": "Accessories", "price": 99.99},
                   {"product_id": 202, "name": "Smartwatch", "category": "Electronics", "price": 299.99}]


@app.get('/product/{product_id}')
async def product_info(product_id: int):
    return [product_info for product_info in sample_products if product_info['product_id'] == product_id][0]


@app.get('/products/search')
async def product_search(keyword: str, category: str = None, limit: int = 10):
    return [product for product in sample_products
            if product['category'] == category and keyword in product['name'].lower()][:limit]


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        data = await websocket.receive_text()
    except WebSocketDisconnect:
        pass



