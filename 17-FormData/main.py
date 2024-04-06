from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Annotated


class UserBase(BaseModel):
    username: Annotated[str, Form(alias='user-name')]
    fullname: Annotated[str, Form()]
    age: Annotated[int, Form()]
    gender: Annotated[str, Form()]


class RegisterIn(UserBase):
    password: Annotated[str, Form(alias='pass_word')]



app = FastAPI()

""" When you want to receive data from form
"""
@app.post('/login')
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {'username': username}

# alias in form
@app.post('/login1')
async def login(username: Annotated[str, Form(alias='user_name')], password: Annotated[str, Form(alias='pass_word')]):
    return {'username': username}



@app.post('/register', response_model=UserBase)
async def login(register: RegisterIn):
    return register


# Practice

@app.post('/registerform')
async def login(username: Annotated[str, Form(alias='user-name')],
                password: Annotated[str, Form(alias='pass_word')],
                fullname: Annotated[str, Form()],
                age: Annotated[int, Form()],
                gender: Annotated[str, Form()]
                ):
    return {'username': username,
            'fullname': fullname,
            'age': age,
            'gender': gender}



@app.post('/registerform1', response_model=UserBase)
async def login(item: Annotated[RegisterIn, Form()]):
    return {"item": item}
