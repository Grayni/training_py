# uvicorn DELETE:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"


from fastapi import FastAPI
from databases import Database
from pydantic import BaseModel

app = FastAPI()


# URL для PostgreSQL
DATABASE_URL = 'postgresql://omenbest:test1234@localhost:5432/mydatabase'

database = Database(DATABASE_URL)


# Модель User для валидации входных данных
class UserCreate(BaseModel):
    username: str
    email: str


# Модель User для валидации исходящих данных (демонстрация)
class UserReturn(BaseModel):
    username: str
    email: str
    id: int | None


@app.on_event('startup')
async def startup_database():
    await database.connect()


@app.on_event('shutdown')
async def shutdown_database():
    await database.disconnect()


# Создание роута для создания пользователя
@app.post('/users/', response_model=UserReturn)
async def create_user(user: UserCreate):
    query = 'INSERT INTO users (username, email) VALUES (:username, :email) RETURNING id'
    values = {'username': user.username, 'email': user.email}
    try:
        user_id = await database.execute(query=query, values=values)
        return {**user.dict(), "id": user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail='Failed to create user')


# роут для удаления информации о юзере по ID
@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    query = "DELETE FROM users WHERE id = :user_id RETURNING id"
    values = {"user_id": user_id}
    try:
        deleted_rows = await database.execute(query=query, values=values)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to delete user from database")
    if deleted_rows:
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")