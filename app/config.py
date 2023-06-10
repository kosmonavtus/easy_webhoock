import os
from typing import Any, Mapping
from dotenv import load_dotenv


load_dotenv()


def get_config() -> Mapping[str, Any]:
    return {
        "GITLAB_TOKEN": os.environ.get("GITLAB_TOKEN", "TEST__token_for__EXAMPLE"),
        "REPO_URL": os.environ.get("REPO_URL"),
        "DEST_DIR": os.environ.get("DEST_DIR")
    }
