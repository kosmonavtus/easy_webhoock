import os
from typing import Any, Mapping
from dotenv import load_dotenv


load_dotenv()

def get_config() -> Mapping[str, Any]:
    return {
        "GITLAB_TOKEN": os.environ.get("GITLAB_TOKEN", "TEST__token_for__EXAMPLE"),
        #"SECRET_KEY_HEX": os.environ.get("SECRET_KEY_HEX"),
    }
