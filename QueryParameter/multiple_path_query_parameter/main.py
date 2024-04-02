from fastapi import FastAPI
app = FastAPI()

@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(
        user_id: int, item_id: str, q: str | None = None, short: bool= False
):
    item = {'item_id': item_id, 'owner_id': user_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update({'description': "This is an amazing item that has a long description"})

    return item

# Required query parameters

# http://127.0.0.1:8000/item/foo-item we must pass http://127.0.0.1:8000/item/foo-item?needy=value or error will come
@app.get('/item/{item_id}')
async def read_user_item(item_id: str, needy: str):
    item = {'item_id': item_id, 'needy': needy}
    return item

@app.get("/item1/{item_id}")
async def read_user_input(
        item_id : str, needy:str, skip:int=0, limit:int | None =None
):
    item = {'item_id': item_id, 'needy': needy, 'skipy': skip, 'limit':limit}
    return item