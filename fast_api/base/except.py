# uvicorn except:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"

from fastapi import FastAPI, HTTPException

app = FastAPI()


# класс кастомного исключения для ошибок
class CustomException(HTTPException):
    def __init__(self, detail: str, status_code: int = 400):
        super().__init__(status_code=status_code, detail=detail)


# пример маршрута, который райзит (выбрасывает) кастомное исключение
@app.get('/items/{item_id}/')
def read_item(item_id: int):
    if item_id == 42:
        raise CustomException(detail="Item not found", status_code=404)
    return {'item_id': item_id}

