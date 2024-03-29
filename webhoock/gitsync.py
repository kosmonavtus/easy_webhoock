from subprocess import run, STDOUT, PIPE
from subprocess import CalledProcessError
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException
from starlette.status import HTTP_403_FORBIDDEN
from webhoock.config import Settings


config = Settings()
api_key_header = APIKeyHeader(name="X-gitlab-Token", auto_error=False)


def get_api_key(api_key_header: str = Security(api_key_header)) -> bool:
    if api_key_header == config.gitlab_token:
        return True
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )


def git_pull() -> dict:
    cmd = ["/usr/local/bin/git", "pull"]
    try:
        output = run(cmd, stdout=PIPE, stderr=STDOUT, text=True, cwd=config.git_work_directory)
        return {"StatusCode": output.returncode}
    except (CalledProcessError, FileNotFoundError, PermissionError) as e:
        raise e
