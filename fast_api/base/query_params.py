# uvicorn query_params:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"

from typing import Annotated
from fastapi import FastAPI, Header

app = FastAPI()


# query
@app.get('/items/')
async def read_items(q: str | None = None): # валидируем и задаем значение по умолчанию
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results


# Path
@app.get('/items/{item_id}')
async def read_item(item_id: int): # задаем тип
    return {'item_id': item_id}


# Header
@app.get('/items2/')
async def read_items2(user_agent: Annotated[str | None, Header()] = None): # задаем тип
    return {'user_agent': user_agent}


