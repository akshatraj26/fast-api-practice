from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, Header


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != 'fake-super-secret-token':
        raise HTTPException(status_code=400, detail="X-token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-key header invalid")
    return x_key

app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/items/")
async def read_items():
    return [{'item': "Foo"}, {"item" : "Bar"}]


@app.get("/users/")
async def read_items():
    return [{'username': "Rick"}, {"username" : "Morty"}]