from typing import Optional
from pydantic import BaseModel, EmailStr, Field, PositiveInt
from fastapi import Form


class User(BaseModel):
    id: int
    name: str
    age: int


class Feedback(BaseModel):
    name: str
    message: str


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: PositiveInt = Field(default=1, lt=130)
    is_subscribed: bool = False
