from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Any

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


# Added an Output model
class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user/")
async def create_user(user: UserIn) -> UserIn:
    return user


@app.post("/user2/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user
