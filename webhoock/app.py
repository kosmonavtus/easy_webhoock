from fastapi import FastAPI
import uvicorn
from webhoock.routes.api import whrouter


def easy_webhoock():
    app = FastAPI()
    app.include_router(whrouter, prefix="/api/v1")
    return app


if __name__ == '__main__':
    app = easy_webhoock()
    uvicorn.run(app, host='0.0.0.0', port=8000)
