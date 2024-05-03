from typing import Annotated, Any
from fastapi import FastAPI, Depends


app = FastAPI()

fake_item_db = [{'item_name': 'Foo'}, {'item_name': 'Bar'}, {'item_name': 'Baz'}]

class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get('/items/')
async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    response = {}
    if commons.q:
        response.update({'q': commons.q})
    items = fake_item_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response

@app.get('/items2/')
async def read_items(commons: Annotated[Any, Depends(CommonQueryParams)]):
    response = {}
    if commons.q:
        response.update({'q': commons.q})
    items = fake_item_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response



# shortcuts
@app.get('/items3/')
async def read_items(commons: Annotated[CommonQueryParams, Depends()]):
    response = {}
    if commons.q:
        response.update({'q': commons.q})
    items = fake_item_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response
