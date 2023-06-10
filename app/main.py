from fastapi import FastAPI
from api import whrouter


def easy_webhoock():
    app = FastAPI()
    app.include_router(whrouter, prefix="/api/v1")
    return app
