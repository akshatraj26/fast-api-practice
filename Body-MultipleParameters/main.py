from fastapi import FastAPI, Path, Body, Query
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None= None


@app.put('/items/{item_id}')
async def update_item(item_id: Annotated[int, Path(title='The ID of the item to get', ge=0, le=1000)],
                      q: str | None = None,
                      item: Item | None = None):
    results = {"item_id": item_id}
    if q:
        results.update({'q': q})
    if item:
        results.update({'item': item})
    return results


# Multiple body paremeters like User and Item
@app.put("items2/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {'item_id': item_id, 'item': item, 'user': user}
    return results


@app.put('items3/{item_id}')
async def update_item(
        item_id: int, item:Item, user:User, importance: Annotated[int, Body()]
):
    results = {'item_id': item_id, 'item': item, 'user': user, 'importance': importance}
    return results


# Multiple body params and query
@app.put('items4/{item_id}')
async def update_item(
        *,
        item_id: int,
        item: Item,
        user: User,
        importance: Annotated[int, Body(gt=0)],
        q: str | None=None
):
    results = {'item_id': item_id, 'item': item,
               'user': user, 'importance': importance,
               }
    if q:
        results.update({'q': q})
    return results


# Embed a single body parameter
@app.put('/items5/{item_id}')
async def update_item(item_id:int,
                      item: Annotated[Item, Body(embed=True)]):
    results = {'item_id': item_id,
               'item': item}
    return results


@app.put('/items6/{item_id}')
async def update_item(item_id: int,
                      user: Annotated[User, Body(embed=True)]):
    results = {'item_id': item_id,
               'user': user}
    return results
