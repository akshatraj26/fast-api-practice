from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# List Types


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.put("/items/{item_id}")
async def update_item(item_id, item: Item):
    results = {'item_id': item_id, 'item': item}
    return results
