# uvicorn validation_types:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"

from fastapi import FastAPI, HTTPException
from models.item import Item

app = FastAPI()


@app.post('/items/')
def create_item(item: Item):
    try:
        if item.price < 0:
            raise ValueError('Price must be non-negative')

        return {'message': 'Item create successfully', 'item': item}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))