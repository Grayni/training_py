# uvicorn READ:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"

from fastapi import FastAPI, HTTPException
from databases import Database
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# URL для PostgreSQL
DATABASE_URL = 'postgresql://omenbest:test1234@localhost:5432/mydatabase'

database = Database(DATABASE_URL)


# Модель User для валидации входных данных
class UserCreate(BaseModel):
    username: str
    email: str


# Модель User для валидации исходящих данных
class UserReturn(BaseModel):
    username: str
    email: str
    id: Optional[int] = None


# Условия подключения и отключения от базы данных
@app.on_event('startup')
async def startup_database():
    await database.connect()


@app.on_event('shutdown')
async def shutdown_database():
    await database.disconnect()


# создание роута для создания юзеров
@app.post('/users/', response_model=UserReturn)
async def create_user(user: UserCreate):
    query = 'INSERT INTO users (username, email) VALUES (:username, :email) RETURNING id'
    values = {'username': user.username, 'email': user.email}
    try:
        user_id = await database.execute(query=query, values=values)
        return {**user.dict(), 'id': user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail='Failed to create user')


# маршрут для получения информации о юзере по ID
@app.get('/users/{user_id}', response_model=UserReturn)
async def get_user(user_id: int):
    query = 'SELECT * FROM users WHERE  id = :user_id'
    values = {'user_id': user_id}
    try:
        result = await database.fetch_one(query=query, values=values)
    except Exception as e:
        raise HTTPException(status_code=500, detail='Failed to fetch user from database')
    if result:
        return UserReturn(username=result['username'], email=result['email'], id=result['id'])
    else:
        raise HTTPException(status_code=404, detail='User not found')
