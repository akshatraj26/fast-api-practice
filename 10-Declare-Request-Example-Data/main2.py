# Field additional arguments
from fastapi import FastAPI
from pydantic import BaseModel, Field
app  = FastAPI()
class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, examples=['A very nice item.'])
    price: float = Field(exclude=[34.5])
    tax: float | None = Field(default=None, exclude=[3.2])


@app.put('/items/{item_id}')
async def update_item(item_id: int, item:Item):
    results = {'item_id': item_id, 'item': Item}
    return results
