from faker import Faker
from random import randint
from dotenv import set_key, dotenv_values
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
ENV_PATH = os.path.join(ROOT_DIR, ".env")

env_vars = dotenv_values(ENV_PATH)

fake = Faker()


class Payloads:

    def generate_user(self):
        user_data = {
            "userName": fake.user_name(),
            "password": fake.password(length=randint(10, 20))
        }

        set_key(ENV_PATH, "USERNAME", user_data["userName"])
        set_key(ENV_PATH, "PASSWORD", user_data["password"])

        print(f"File .env was updated: {ENV_PATH}")
        return user_data
