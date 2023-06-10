from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    gitlab_token: str = "TEST__token_for__EXAMPLE"
    gitlab_repo_url: str
    git_work_directory: str
