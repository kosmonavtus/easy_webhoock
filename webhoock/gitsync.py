from subprocess import run, STDOUT, PIPE
from subprocess import CalledProcessError


def git_pull(git_repo_dir: str) -> dict:
    cmd = ["git", "pull"]
    try:
        output = run(cmd, stdout=PIPE, stderr=STDOUT, text=True, cwd=git_repo_dir)
        return {"StatusCode": output.returncode}
    except CalledProcessError:
        raise CalledProcessError.stderr
    except FileNotFoundError:
        raise FileNotFoundError
    except PermissionError:
        raise PermissionError
