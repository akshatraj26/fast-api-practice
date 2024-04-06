from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post('/files/')
async def create_files(files: Annotated[list[bytes], File()]):
    return {'file_sizes': [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {'filenames': {file.filename: file.size for file in files}}



# Multiple file uploads with additional metadata
@app.post('/files1/')
async def create_files(files: Annotated[list[bytes], File(description="Multiple files as bytes")]):
    return {'file_sizes': [len(file) for file in files]}


@app.post("/uploadfiles1/")
async def create_upload_files(files: Annotated[list[UploadFile], File(description="Multiple files as UploadFile")]):
    return {'filenames': {file.filename: file.size for file in files}}

@app.get("/")
async def main():
    content = """
    <body>
    <form action="/files/" enctype="multipart/form-data" method="post">
    <label>Multiple File Upload</label>
    <input name='files' type='file' multiple>
    <input type="submit">
    </form>
    
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
    <label>Multiple UploadFiles Upload</label>
    <input name='files' type='file' multiple>
    <input type="submit">
    </form>
    
    
    <form action="/files1/" enctype="multipart/form-data" method="post">
    <label>Multiple File Upload with additional metadata</label>
    <input name='files' type='file' multiple>
    <input type="submit">
    </form>
    
    <form action="/uploadfiles1/" enctype="multipart/form-data" method="post">
    <label>Multiple Upload Upload with additional metadata</label>
    <input name='files' type='file' multiple>
    <input type="submit">
    </form>
    
    </body>
    """
    return HTMLResponse(content=content)