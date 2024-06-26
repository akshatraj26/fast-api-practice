from typing import Annotated

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

fake_secret_token = 'coneofsilence'

fake_db = {
    "foo": {'id': "foo", 'title': "FOO", "description": "There goes my hero"},
    "bar": {'id': 'bar', 'title': "BAR", "description": "The bartenders"}
}

app = FastAPI()

class Item(BaseModel):
    id: str
    title: str
    description: str | None = None

@app.get("/items/{item_id}", response_model=Item)
async def read_main(item_id: str, x_token: Annotated[str, Header()]):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]


@app.post("/items/", response_model=Item)
async def create_item(item: Item, x_token: Annotated[str, Header()]):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_db[item.id] = Item
    return item

