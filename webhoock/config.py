from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    gitlab_token: str = "oodai9AhFoodeethooneiv0iequu4buethohr5ife9"
    gitlab_repo_url: str
    git_work_directory: str = '/srv/salt'

    class Config:
        env_file = ".env"
