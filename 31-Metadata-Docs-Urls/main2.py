from fastapi import FastAPI

tags_metadata = [
    {
        'name': 'users',
        "description": "Operations with users. The **login** logic is also here."
    },
    {
        'name': 'items',
        "description": 'Manage items. so _fancy_  they have  their own docs.',
        'externalDocs': {
            'description': "Item external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(openapi_tags=tags_metadata, )





@app.get("/items/", tags=['items'])
async def get_items():
    return [{'name': 'want'}, {'name': 'flying broom'}]

@app.get("/users/", tags=['users'])
async def get_users():
    return [{"name": "Harry"},
            {'name': "Ron"}
            ]
