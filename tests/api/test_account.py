import allure
import pytest
from config.base_test import BaseTest

uuid = []


@allure.epic("Administration")
@allure.feature("Users")
class TestAccount(BaseTest):

    @allure.title("Create a new user")
    def test_create_user(self):
        user = self.api_account.create_user()
        uuid.append(user.userID)

    @allure.title("Auth user")
    def test_auth_user(self):
        self.api_account.auth_user()

    @allure.title("Get user info")
    def test_get_user_info(self):
        self.api_account.get_user_by_id("".join(uuid))
