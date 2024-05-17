# uvicorn model_except2:app --reload --reload-include="*.html" --reload-include="*.css" --reload-include="*.js"

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from models.err import CustomExceptionModel

app = FastAPI()


class ItemsResponse(BaseModel):
    item_id: int


class CustomException(HTTPException):
    def __init__(self, detail: str, status_code: int, message: str):
        super().__init__(status_code=status_code, detail=detail)
        self.message = message


@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException) -> JSONResponse:
    error = jsonable_encoder(
        CustomExceptionModel(status_code=exc.status_code, er_message=exc.message, er_details=exc.detail))
    return JSONResponse(status_code=exc.status_code, content=error)


@app.get(
    "/items/{item_id}/",
    response_model=ItemsResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Items by ID.",
    description="The endpoint returns item_id by ID. If the item_id is 42, an exception with the status code 404 is returned.",
    responses={
        status.HTTP_200_OK: {'model': ItemsResponse},
        status.HTTP_404_NOT_FOUND: {'model': CustomExceptionModel},  # вот тут применяем схемы ошибок пидантика
    },
)
async def read_item(item_id: int):
    if item_id == 42:
        raise CustomException(detail="Item not found", status_code=404,
                              message="You're trying to get an item that doesn't exist. Try entering a different item_id.")
    return ItemsResponse(item_id=item_id)