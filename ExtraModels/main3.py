from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type: str = "Car"


class PlaneItem(BaseItem):
    type: str = 'plane'
    size: int


items = {
    'item1': {'description': 'All my friends drive a low rider', 'type': 'car'},
    'item2':  {'description': "Music is my aeroplane, it's my aeroplane",
               'size': 5,
               'type': 'plane'},
}


@app.get("/items/{item_id}", response_model=Union[CarItem, PlaneItem])
async def read_item(item_id: str):
    return items[item_id]


