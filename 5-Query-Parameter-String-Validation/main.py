from fastapi import FastAPI, Query
import fastapi
from typing import Annotated
app = FastAPI()
@app.get('/items/')
async def read_items(q:Annotated[str | None, Query(max_length=50)] = None):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}, {'fast_api_version': fastapi.__version__}]}
    if q:
        results.update({'q':q})
    return results

@app.get('/items2/')
async def read_items(q:str | None= Query(default= None, max_length=50)):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}, {'fast_api_version': fastapi.__version__}]}
    if q:
        results.update({'q':q})
    return results

@app.get('/default/')
async def read_items(q:Annotated[str, Query()] = 'Rick'):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}, {'fast_api_version': fastapi.__version__}]}
    if q:
        results.update({'q':q})
    return results

# Add more validations

@app.get('/min/')
async def read_items(q: Annotated[str | None, Query(min_length=4, max_length=50)] = None):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q':q})
    return results

# Add regular expressions
@app.get('/pattern/')
async def read_items(q: Annotated[str | None, Query(min_length=4, max_length=50, pattern="^fixedquery$")] = None):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results

# Add regex expressions
@app.get('/reg/')
async def read_items(q: Annotated[str | None, Query(min_length=4, max_length=50, regex="^fixedquery$")] = None):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results


# Default values
@app.get('/def/')
async def read_items(q: Annotated[str, Query(min_length=4)] = 'nothing is in here'):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results

# required value using Query
@app.get('/req/')
async def read_items(q: Annotated[str, Query(min_length=4)]):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results


# Required with Ellipsis
@app.get('/ellip/')
async def read_items(q: Annotated[str, Query(min_length=4)] = ...):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results

# Required with None
@app.get('/non/')
async def read_items(q: Annotated[str | None, Query(min_length=4)] = ...):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results


# Query parameter list / multiple values
@app.get('/using_list/')
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {'q': q}
    return query_items

# http://localhost:8000/items/?q=foo&q=bar


# Query parameter list / multiple values with defaults
@app.get('/mul_def/')
async def read_items(q: Annotated[list[str], Query()] = ['Akshat', 'Amog']):
    query_items = {'q': q}
    return query_items


# Using list¶
@app.get('/use_list_dir/')
async def read_items(q: Annotated[list, Query()] = []):
    query_items = {'q': q}
    return query_items


# Declare more metadata
# You can add a title

@app.get('/title/')
async def read_items(q: Annotated[str | None, Query(title='Query String', min_length=4)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Declare more metadata
# You can add a title, description

@app.get('/des/')
async def read_items(q: Annotated[str | None, Query(title='Query String',
                                                    description="Query string for the items to search \
                                                                in the database that have a good match",
                                                    min_length=4)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Alias parameters
@app.get('/alia/')
async def read_items(q: Annotated[str | None, Query(alias='item-query')] = None):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Boo'}]}
    if q:
        results.update({'q': q})

    return results

# depricated meta data
@app.get('/dep/')
async def read_items(q: Annotated[str | None, Query(alias='item-query',
                                                    title='Query-string',
                                                    description="Query string for the items to search in the database that have a good match",
                                                    min_length=3,
                                                    max_length=50,
                                                    pattern= "^fixedquery$",
                                                    deprecated=True)] = None):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Boo'}]}
    if q:
        results.update({'q': q})

    return results


# Exclude from OpenAPI
@app.get('/exec_openapi/')
async def read_items(hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Boo'}]}
    if hidden_query:
        return {'hidden_query': hidden_query}
    else:
        return {'Not found'}
