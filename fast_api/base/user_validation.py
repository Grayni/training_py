# uvicorn user_validation:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from models.user import User

app = FastAPI()


custom_messages = {
    "username": "Имя должно быть строкой",
    "age": "Возраст должен быть более 18",
    "email": "Ошибка в записи email",
    "password": "Длина пароля должна быть от 8 до 16 символов",
    "phone": "В качестве номера телефона ожидается строка",
}


@app.exception_handler(RequestValidationError)
def custom_request_validation_handler(reqeust: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        field = error['loc'][-1]
        msg = custom_messages.get(field)
        errors.append({'field': field, 'msg': msg, 'value': error['input']})
    print(errors)
    return JSONResponse(status_code=400, content=errors)


@app.post('/users/')
async def post_user(user: User):
    return user

