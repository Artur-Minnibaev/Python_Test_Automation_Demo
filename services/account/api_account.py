import os
import requests
import allure
from utils.helper import Helper
from services.account.payloads import Payloads
from services.account.endpoints import Endpoints
from config.headers import Headers
from services.account.models.account_model import AccountModel
from dotenv import load_dotenv

load_dotenv()


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
            json=self.payloads.create_user
        )
        assert response.status_code == 201, response.json()
        self.attach_response(response.json())
        model = AccountModel(**response.json())
        return model

    @allure.step("Auth user")
    def auth_user(self):
        response = requests.post(
            url=self.endpoints.auth_user,
            headers=self.header.basic,
            json={
                "userName": os.environ.get("USERNAME"),
                "password": os.environ.get("PASSWORD")
            }
        )
        assert response.status_code == 200, response.json()
        assert response.json() == True, response.json()
        self.attach_response(response.json())
        return response

    @allure.step("Get user uuid")
    def get_user_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_id(UUID=uuid),
            headers=self.header.basic,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = AccountModel(**response.json())
        return model
