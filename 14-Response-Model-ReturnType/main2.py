from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post('/item/', response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get('/items/', response_model=list[Item])
async def read_items() -> Any:
    return [
        {'name': 'Saket', "price": 42.5},
        {'name': "Plumbus", 'price': 32.0},
    ]

