import allure
from services.db.database import PostgreSQL
from services.account.api_account import AccountAPI


@allure.epic("Integration tests")
@allure.feature("DB")
class TestIntegration:
    @allure.step("Create/check Table Books(items_app)")
    def test_create_books_table(self, set_up_db):
        if PostgreSQL.books_table_exist(set_up_db):
            print("[INFO]Table 'items_app' already exists")
        else:
            PostgreSQL.create_book_table(set_up_db)
            assert PostgreSQL.books_table_exist(set_up_db), "[FAIL]Table was not created"
            print("[INFO]Table items_app created successfully")

    @allure.step("Create/check Table User(user_table)")
    def test_create_user_table(self, set_up_db):
        if PostgreSQL.user_table_exist(set_up_db):
            print("[INFO]Table 'user_table' already exists")
        else:
            PostgreSQL.create_user_table(set_up_db)
            assert PostgreSQL.user_table_exist(set_up_db), "[FAIL]Table was not created"
            print("[INFO]Table items_app created successfully")

    @allure.step("Insert data into User Table(user_table)")
    def test_insert_user_data_into_db(self, set_up_db):
        api_client = AccountAPI()
        response_data = api_client.login_user()

        assert response_data.status_code == 200, f"[FAIL]Incorrect request: {response_data.status_code}, {response_data.json()}"

        user_data = response_data.json()
        PostgreSQL.insert_user(set_up_db, user_data)
        set_up_db.execute("SELECT * FROM user_table WHERE userId = %s", (user_data["userId"],))
        result = set_up_db.fetchone()

        assert result is not None, "[FAIL]User wasn't insert into DB"

        print(f"[PASS]Data of new User {user_data['username']} was saved into DB successfully.")
