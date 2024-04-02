from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': dir(app)}


@app.options('/demographic')
async def demographic():
    return {
        'FName': 'Amogsiddha',
        'LName': 'Deshmukh',
        'Address': 'Nagpur',
        'Gender': 'Male',
        'Height': 5.6,
        'Weight': 79,
        'Eye color': 'Black',
        'Body type': 'Healthy',
    }

# Path Parameters: Get item by Id
@app.get('/items/{item_id}')
async def read_item(item_id : int):
    return {'item_id' : item_id}
