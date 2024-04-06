from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post('/items/')
async def create_item(item : Item) -> Item:
    return item


@app.get('/items/')
async def read_items() -> list[Item]:
    return [
        Item(name='Portal Gun', price=42.0, description='I am gay but I can tell anybody. If i do people will make fun '
                                                        'of me. So I am writing it in my code. so no one will know.'),
        Item(name='Plumbus', price=32.0),
        Item(name='Plumbus') # because of this line I will get internal server error. price field is empty
    ]

