from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post('/items/')
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})

    return item_dict


@app.put('/items/{items_id}')
async def create_item(items_id: int, item: Item):
    return {'items_id': items_id, **item.dict()}


# second put
@app.put('/items2/{items_id}')
async def update_item(items_id: int, item: Item, q:str | None = None):
    result = {'item_id': items_id, **item.dict()}
    if q:
        result.update({'q': q})
    return result