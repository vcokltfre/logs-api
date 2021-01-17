from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from starlette.responses import PlainTextResponse

from src.store import Storage
from src.models import NewData
from src.auth import auth

app = FastAPI(docs_url=None)
store = Storage()

@app.post("/new")
async def new_post(data: NewData, req: Request):
    auth(req)

    return {"status":"ok", "url":await store.new(data.text, data.name, data.timeout)}

@app.get("/logs/{pageid}")
async def get_post(pageid: str):
    d = await store.get(pageid)

    if not d:
        return HTTPException(404, "Page not found.")

    return PlainTextResponse(d)