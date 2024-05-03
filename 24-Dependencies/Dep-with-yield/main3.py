# Always raise in Dependencies with yield and except
# Dependencies with yield and except
from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


app = FastAPI()


class InternalError(Exception):
    pass

def get_username():
    try:
        yield 'Rick'
    except InternalError:
        print("We don't swallow the internal error here, we raise again 😎")
        raise


@app.get("/items/{item_id}", dependencies=[Depends(get_username), Depends(oauth2_schema)])
def get_items(item_id: str, username: Annotated[str, Depends(get_username)]):
    if item_id == "portal-gun":
        raise InternalError(f"The Portal Gun is to dangerous to be owned by {username}")
    if item_id != "plumbus":
        raise HTTPException(status_code=404, detail="Item not found, there's only plumbus here")
    return item_id
