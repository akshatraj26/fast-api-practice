# Response with arbitrary dict
from fastapi import FastAPI


app = FastAPI()


@app.get("/keywords-weights/", response_model=dict[str, float])
async def read_keyword_weights():
    return {'foo': 2.324, 'bar': 234.35}
