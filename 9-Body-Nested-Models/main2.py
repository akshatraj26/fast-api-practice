from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []


@app.put('/items/{item_id}')
async def update_item(item_id:int, item: Item):
    results = {'item_id': item_id, 'item': Item}
    return results