from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

# Import Path
@app.get('/items/{item_id}')
async def read_items(item_id: Annotated[int, Path(title="The ID of the item to get")],
                     q: Annotated[str | None,  Query(alias='item-query')] = None):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results

# Declare metadata
# Order the parameters as you need
@app.get('/items1/{item_id}')
async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results



# * for the key-value pair

@app.get('/items2/{item_id}')
def read_items(*, item_id: int = Path(title='The IP of the item to get'), q:str):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results


# Number validations: greater than or equal
@app.get('/items3/{item_id}')
def read_items(item_id: Annotated[int, Path(title='The IP of the item to get', ge=2)], q:str):
    results = {'item_id': item_id}
    if q:
        results.update({'q':q})
    return results

# Number validations: greater than and less than or equal
@app.get('/items4/{item_id}')
def read_items(item_id: Annotated[int, Path(title='The IP of the item to get', gt=0, le=1000)], q: str):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results

# Number validations: floats, greater than and less than
@app.get('/items5/{item_id}')
def read_items(item_id: Annotated[int, Path(title='The IP of the item to get', ge=0, le=1000)],
               q: str,
               size: Annotated[float, Query(ge=0, lt=10.5)]):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    if size:
        results.update({'size': size})
    return results

