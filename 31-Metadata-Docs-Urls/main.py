from fastapi import FastAPI

description = """This is my custom description. I wrote whatever i desired. 

**I am working on a fastapi**.
I am building a api that will work everywhere.
 
 `and I will be the owner` of this api"""

description = """
ChimichangApp API helps you do awesome stuff.

## Items

You can **read items**.


## User

You will be able to:

* **Create User**
* **Inject Dependencies**
* **Read User**
* `Update Data`
* `Deploy you API`"""

app = FastAPI(title="АКШАТРАДЖ И ЕГО ДРУГ",
              description=description,
              summary="Deadpool's favourite application is Application.",
              version='0.0123.23234',
              terms_of_service="http://example.com/terms/",
              contact={
                  "name": 'Akshat Listener and Data Scientist',
                  'url': "http://x-force.example.com/contact/",
                  'email': 'akshatraj2607@gmail.com'
              },
              license_info={
                  'name': "Apache 2.0",
                  'url': "https://www.apache.org/licenses/LICENSE-2.0.html"
              }
              )

app = FastAPI(title="АКШАТРАДЖ И ЕГО ДРУГ",
              description=description,
              summary="Deadpool's favourite application is Application.",
              version='0.0123.23234',
              terms_of_service="http://example.com/terms/",
              contact={
                  "name": 'Akshat Listener and Data Scientist',
                  'url': "http://x-force.example.com/contact/",
                  'email': 'akshatraj2607@gmail.com'
              },
              license_info={
                  'name': "Apache 2.0",
                  'identifier': "MIT"
              }
              )


@app.get("/items/")
async def read_items():
    return [{'name': "Saket Saurabh"}]