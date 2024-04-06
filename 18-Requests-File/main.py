# Request Files
from fastapi import FastAPI, File, UploadFile
from typing import Annotated

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {
        "file-size": f"{len(file)} bytes",
        "file-size-mb": f"{len(file) / 2 ** 20} mb",
        "file-size-kb": f"{len(file) * 0.001} kb"}


@app.post("/uploadfile/")
async def upload_file(file: UploadFile):
    return {'filename': file.filename,
            'filesize': file.size,
            'filedetails': file.headers,
            'file': file.file,
            'content-type': file.content_type,
            }


# upload the optional option


@app.post("/files1/")
async def create_file(file: Annotated[bytes | None, File()] = None):
    if not file:
        return {"messages": "No file sent"}
    else:
        return {
            "file-size": f"{len(file)} bytes",
            "file-size-mb": f"{len(file) / 2 ** 20} mb",
            "file-size-kb": f"{len(file) * 0.001} kb"}


@app.post("/uploadfile1/")
async def upload_file(file: UploadFile | None = None):
    if not file:
        return {'messages': "No upload file sent"}
    else:
        return {'filename': file.filename,
                'filesize': file.size,
                'filedetails': file.headers,
                'file': file.file,
                'content-type': file.content_type,
                }

# Upload file with additional metadata

@app.post("/files3/")
async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
    return {
        "file-size": f"{len(file)} bytes",
        "file-size-mb": f"{len(file) / 2 ** 20} mb",
        "file-size-kb": f"{len(file) * 0.001} kb"}


@app.post("/uploadfile3/")
async def upload_file(file: Annotated[UploadFile, File(description="A file read as UploadFile")]):
    return {'filename': file.filename,
            'file': file.file,
            'content-type': file.content_type,
            }
