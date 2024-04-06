from typing import Annotated
from fastapi import FastAPI, Header

app = FastAPI()


@app.get('/items/')
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}

# to disable the automatic conversion of _ to -


@app.get('/items1/')
async def read_items(strange_header: Annotated[str | None, Header(convert_underscores=False)] = None):
    return {"strange_header": strange_header}


@app.get("/items2/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {'X-Token values': x_token}


