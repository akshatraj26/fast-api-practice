from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel


app = FastAPI()


class Tags(Enum):
    items = 'items'
    users = 'users'


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.get("/items/", tags=[Tags.items])
async def get_items():
    return ["Portal Gun", "Plumbus"]


@app.get('/user/', tags=[Tags.users])
async def read_users():
    return ['Rick', "Morty"]


# Summary and Description
@app.post("/items/", summary="Create an Item",
          response_model=Item,
          description="Create an item with all the information, name, description, price, tax and a set of unique tags")
async def create_item(item: Item):
    return item


# Description from Docstring  and Response description
@app.post("/items2/", response_model=Item, summary="create an item", response_description="The Created Item")
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a `long description`
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item