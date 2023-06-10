import uvicorn
from webhoock.app import easy_webhoock


if __name__ == "__main__":
    app = easy_webhoock()
    uvicorn.run(app, host='0.0.0.0', port=8000)
