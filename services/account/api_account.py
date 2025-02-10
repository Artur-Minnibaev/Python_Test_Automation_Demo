import os
import requests
import allure
from utils.helper import Helper
from services.account.payloads import Payloads, ENV_PATH
from services.account.endpoints import Endpoints
from config.headers import Headers
from services.account.models.account_model import AccountModel
from dotenv import load_dotenv, dotenv_values, set_key

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
ENV_PATH = os.path.join(ROOT_DIR, ".env")


class AccountAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.header = Headers()

    @allure.step("Create user")
    def create_user(self):
        response = requests.post(
            url=self.endpoints.post_create_user,
            headers=self.header.basic,
            json=self.payloads.generate_user()
        )
        assert response.status_code == 201, response.json()
        self.attach_response(response.json())
        model = AccountModel(**response.json())
        return model

    @allure.step("Auth user")
    def auth_user(self):
        env_vars = dotenv_values(ENV_PATH)
        response = requests.post(
            url=self.endpoints.auth_user,
            headers=self.header.basic,
            json={
                "userName": env_vars.get("USERNAME"),
                "password": env_vars.get("PASSWORD")
            }
        )
        if response .status_code != 200:
            raise AssertionError(f"Exception in auth: {response.status_code}, {response.json()}")

        assert isinstance(response.json(), bool), f"Incorrect response's format: {response.json()}"
        assert response.json() is False, "User is not authorized"
        self.attach_response(response.json())
        return response

    @allure.step("Get TOKEN")
    def generate_token(self):
        env_vars = dotenv_values(ENV_PATH)
        response = requests.post(
            url=self.endpoints.generate_token,
            headers=self.header.basic,
            json={
                "userName": env_vars.get("USERNAME"),
                "password": env_vars.get("PASSWORD")
            }
        )
        assert response.status_code == 200, f"[FAIL]Error generating TOKEN: {response.json()}"
        token = response.json().get("token")
        set_key(ENV_PATH, "API_TOKEN", token)
        load_dotenv()
        os.environ["API_TOKEN"] = token
        assert token, "[FAIL]API did not respond a TOKEN"
        print(f"TOKEN was received: {token}")
        return token

    @allure.step("Get user uuid")
    def get_user_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_id(UUID=uuid),
            headers=self.header.auth_required,
        )
        assert response.status_code == 200, response.json()
        response_json = response.json()
        print(f"[DEBUG]JSON: {response_json}")

        self.attach_response(response.json())
        model = AccountModel(**response.json())
        return model
