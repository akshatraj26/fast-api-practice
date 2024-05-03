from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


app = FastAPI()


def fake_decode_token(token):
    return User(username=token + 'fakedecoded', email='akshatraj2607@mail.com', full_name="Akshat Raj")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = get_current_user()
    return user


@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
