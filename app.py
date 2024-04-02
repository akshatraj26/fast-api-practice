from fastapi import FastAPI

app = FastAPI()
# print(app)
# print(vars(app))
# print(dir(app))

@app.get('/')
async def root():
    return {"message" : 'Hello World\n',
            "My Crush" : '',
            "But he is": 'Straight'}