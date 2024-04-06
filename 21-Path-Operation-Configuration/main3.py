# deprecate a path operation
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/", tags=['items'])
async def read_items():
    return [{"name": 'Dmitry', 'price': 43}]


@app.get("/user/", tags=['users'])
async def read_users():
    return [{"username": "johndoe"}]


@app.get("/elements/", tags=['items'], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]
