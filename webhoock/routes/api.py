import http
from fastapi import APIRouter
from fastapi import Request
from fastapi import Response
from fastapi import HTTPException
from webhoock.hmac_signatuer import verify_hmac
from webhoock.hmac_signatuer import generate_secret_key
from webhoock.hmac_signatuer import make_hmac_signature
from webhoock.gitsync import git_pull
from webhoock.config import Settings


is_viewed = False
setting = Settings()  # type: ignore
exepted_token = make_hmac_signature(generate_secret_key(), setting.gitlab_token)


whrouter = APIRouter()


@whrouter.post("/webhook")
def webhook(requset: Request, response: Response) -> dict:
    received_token = requset.headers.get("X-gitlab-Token")
    if not received_token:
        raise HTTPException(status_code=http.HTTPStatus.UNAUTHORIZED, detail='Missing token')
    if not verify_hmac(received_token, exepted_token):
        raise HTTPException(status_code=http.HTTPStatus.UNAUTHORIZED, detail="Invalid token")
    try:
        response.headers["Content-Type"] = "application/json"
        response.status_code = 202
        return git_pull(setting.git_work_directory)
    except Exception as e:
        response.status_code = 500
        return {"Exception": e}


@whrouter.get("/token")
def get_token(request: Request) -> dict:
    global is_viewed
    client_ip = request.client.host
    if not is_viewed and client_ip == "127.0.0.1":
        is_viewed = True
        return {"X-gitlab-Token": exepted_token}
    else:
        raise HTTPException(status_code=http.HTTPStatus.UNAUTHORIZED, detail="Unauthorized")
