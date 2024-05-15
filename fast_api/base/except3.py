# uvicorn except3:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()


class CustomException(HTTPException):
    def __init__(self, detail: str, status_code: int = 400):
        super().__init__(status_code=status_code, detail=detail)


# обработчик ошибок (error handler) для класса CustomException
@app.exception_handler(CustomException)
def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


# обработчик глобальных исключений, который "ловит" все необработанные исключения
@app.exception_handler(Exception)
def custom_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={'error': 'Internal Server Error'}
    )


# добавили непредусмотренное исключение
@app.get("/items/{item_id}/")
def read_item(item_id: int):
    # симулируем непредусмотренное исключение
    result = 1 / 0
    return {"item_id": item_id}