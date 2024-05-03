# Dependencies with yield and HTTPException

from fastapi import Depends, FastAPI, HTTPException
from typing import Annotated

app = FastAPI()

data = {
    "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
    "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
}

print(data["portal-gun"])

class OwnerError(Exception):
    pass


def get_username():
    try:
        yield "Rick"
    except OwnerError as e:
        raise HTTPException(status_code=400, detail=f"Owner Error: {e}")


@app.get("/items/{item_id}")
async def get_items(item_id: str, username: Annotated[str, Depends(get_username)]):
    if item_id not in data:
        raise HTTPException(status_code=404, detail="Item not found")
    item = data[item_id]
    print(item)
    if item['owner'] != username:
        raise OwnerError(username)
    return item
