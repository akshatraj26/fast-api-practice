# Return a response directly
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://youtu.be/b_esvvCzwtg?si=zLD-m5EFEQwN89zI")
    return JSONResponse({'message': "Here is your interdimensional portal"})


# Annotate a response subclass
@app.get('/teleport')
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@app.get("/portal1", response_model=None)
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://youtu.be/b_esvvCzwtg?si=zLD-m5EFEQwN89zI")
    return JSONResponse({'message': "Here is your interdimensional portal"})

