from fastapi import Request
from fastapi.exceptions import HTTPException
from os import environ
from hmac import compare_digest

def auth(req: Request):
    token = req.headers.get("Authorization", None)

    if not compare_digest(token, environ["TOKEN"]):
        raise HTTPException(403, "Not authorized.")
