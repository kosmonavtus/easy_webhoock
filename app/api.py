import http
from fastapi import APIRouter
from fastapi import Request
from fastapi import Response
from fastapi import HTTPException
from app.config import get_config
from hmac_signatuer import verify_hmac
from hmac_signatuer import generate_secret_key
from hmac_signatuer import make_hmac_signature
from subprocess import run, STDOUT, PIPE


is_viewed = False
B_SECRET_KEY = generate_secret_key()
exepted_token = make_hmac_signature(B_SECRET_KEY, get_config()['GITLAB_TOKEN'])
git_repo_dir = get_config()['DEST_DIR']


whrouter = APIRouter


@whrouter.post("/webhook", status_code=http.HTTPStatus.ACCEPTED)
def webhook(requset: Request, response: Response) -> dict:
    received_token = requset.headers.get("X-gitlab-Token")
    if not received_token:
        raise HTTPException(status_code=http.HTTPStatus.UNAUTHORIZED, detail='Missing token')
    if not verify_hmac(received_token, exepted_token):
        raise HTTPException(status_code=http.HTTPStatus.UNAUTHORIZED, detail="Invalid token")
    try:
        cmd = ["git", "pull"]
        output = run(cmd, stdout=PIPE, stderr=STDOUT, text=True, cwd=git_repo_dir)
        outlist = output.stdout.strip('\n').split('\n')
        response.headers["Content-Type"] = "application/json"
        response.status_code = 202
        return {"Stdout": outlist, "Stderror": output.stderr}
    except Exception as e:
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
