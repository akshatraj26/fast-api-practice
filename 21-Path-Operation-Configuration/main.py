from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return item


# tags in path operation

@app.post("/items2/", response_model=Item, tags=['items'])
async def create_item(item: Item):
    return item



@app.get("/items2/", tags=['items'])
async def read_items():
    return [{'name': "Foo", "price": 42}]


@app.get("/users/", tags=['users'])
async def read_users():
    return {'username': 'johndoe'}


