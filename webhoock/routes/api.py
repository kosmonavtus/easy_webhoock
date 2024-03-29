from fastapi import APIRouter
from fastapi import Response
from fastapi import Depends
from webhoock.gitsync import get_api_key
from webhoock.gitsync import git_pull


whrouter = APIRouter(dependencies=[Depends(get_api_key)])


@whrouter.post("/webhook")
def webhook(response: Response) -> dict:
    try:
        response.status_code = 202
        return git_pull()
    except Exception as e:
        response.status_code = 500
        raise e
