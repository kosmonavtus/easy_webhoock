from fastapi import FastAPI, Request, Response, HTTPException
import http
from config import get_config
from hmac_signatuer import make_hmac_signature, generate_secret_key, verify_hmac


app = FastAPI()


gitlab_token = get_config()['GITLAB_TOKEN']
SECRET_KEY_B = generate_secret_key()


@app.post("/webhook", status_code=http.HTTPStatus.ACCEPTED)
async def webhook(requset: Request, response: Response) -> dict:
    received_token = requset.headers.get("X-gitlab-Token")
    if not received_token:
        raise HTTPException(status_code=http.HTTPStatus.UNAUTHORIZED, detail='Missing token')
    if not verify_hmac(received_token, gitlab_token, SECRET_KEY_B):
        raise HTTPException(status_code=http.HTTPStatus.UNAUTHORIZED, detail="Invalid token")
    return {"Result": "Done"}


@app.get("/token")
def get_token(request: Request) -> dict:
    client_ip = request.client.host
    if client_ip != "127.0.0.1":
        raise HTTPException(
            status_code=http.HTTPStatus.UNAUTHORIZED,
            detail="Unauthorized")
    token = make_hmac_signature(SECRET_KEY_B, gitlab_token)
    return {"token": token}
