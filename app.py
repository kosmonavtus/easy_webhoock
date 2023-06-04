from fastapi import FastAPI, Request, Response, HTTPException
import http
from config import get_config
from hmac_signatuer import make_hmac_signature, generate_secret_key, verify_hmac


app = FastAPI()


B_SECRET_KEY = generate_secret_key()


exepted_token = make_hmac_signature(B_SECRET_KEY, get_config()['GITLAB_TOKEN'])


@app.post("/webhook", status_code=http.HTTPStatus.ACCEPTED)
async def webhook(requset: Request, response: Response) -> dict:
    received_token = requset.headers.get("X-gitlab-Token")
    if not received_token:
        raise HTTPException(status_code=http.HTTPStatus.UNAUTHORIZED, detail='Missing token')
    if not verify_hmac(received_token, exepted_token):
        raise HTTPException(status_code=http.HTTPStatus.UNAUTHORIZED, detail="Invalid token")
    return {"Result": "Done"}


@app.get("/token")
def get_token(request: Request) -> dict:
    client_ip = request.client.host
    if client_ip != "127.0.0.1":
        raise HTTPException(
            status_code=http.HTTPStatus.UNAUTHORIZED,
            detail="Unauthorized")
    return {"token": exepted_token}
