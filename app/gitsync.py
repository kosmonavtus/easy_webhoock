from subprocess import run, STDOUT, PIPE
from subprocess import CalledProcessError


def git_pull(git_repo_dir: str) -> dict[bool, list[str]]:
    stderror = list()
    cmd = ["git", "pull"]
    try:
        output = run(cmd, stdout=PIPE, stderr=STDOUT, text=True, cwd=git_repo_dir)
        stdout = output.stdout.strip('\n').split('\n')
        stderror = output.stderr.strip('\n').split('\n')
        return {True: stdout}
    except CalledProcessError:
        return {False: stderror}
    except FileNotFoundError:
        return {False: stderror}
    except PermissionError:
        return {False: stderror}
