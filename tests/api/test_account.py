import allure
from config.base_test import BaseTest

uuid = []


@allure.epic("Administration")
@allure.feature("Users")
class TestAccount(BaseTest):

    @allure.title("Create a new user")
    def test_create_user(self):
        user = self.api_account.create_user()
        assert user.normalized_user_id, "[FAIL]UserID didn't receive"
        uuid.append(user.userID)
        print(uuid)
        print(f"[PASS]User was created: UserName: {user.username}, UserID: {user.userID}")

    @allure.title("Auth user")
    def test_auth_user(self):
        self.api_account.auth_user()

    @allure.title("Get user info")
    def test_get_user_info(self):
        token = self.api_account.generate_token()
        assert token, "[FAIL]API did not respond a TOKEN"

        user_id = uuid[0]
        response = self.api_account.get_user_by_id(user_id)
        assert response.normalized_user_id == user_id, "[FAIL]ID does not match"
