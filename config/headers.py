import os
from dotenv import load_dotenv, dotenv_values

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
ENV_PATH = os.path.join(ROOT_DIR, ".env")


class Headers:
    basic = {
        "Content-Type": "application/json",
    }

    @property
    def auth_required(self):
        load_dotenv(ENV_PATH)
        env_vars = dotenv_values(ENV_PATH)

        current_token = env_vars.get("API_TOKEN", "")
        os.environ["API_TOKEN"] = current_token

        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {current_token}"
        }
