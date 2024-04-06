# HTTP Exception

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteException


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()

items = {'foo': "The Foo Wrestlers"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {'item': items[item_id]}

# Add custom headers
@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404,
                            detail="Item not found",
                            headers = {"X-Error": "There goes my error"},
        )
    return {'item': items[item_id]}


# Custom Exception handler

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request,
                                    exc: UnicornException):
    return JSONResponse(status_code=418,
                        content={'message': f"OOPs! {exc.name} did something. There goes a rainbow..."})


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {'unicorn_name': name}


# Override the default exception exceptions Validation

@app.exception_handler(StarletteException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/items1/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {'item_id': item_id}