import allure


class PostgreSQL:

    @staticmethod
    @allure.step("Creating a Books Table(items_app)")
    def create_book_table(cursor):
        """Create a Book table (if is not exist)"""
        query = """
        CREATE TABLE IF NOT EXISTS items_app (
            id SERIAL PRIMARY KEY,
            isbn TEXT,
            title TEXT,
            subTitle TEXT,
            author TEXT,
            publish_date TIMESTAMP,
            publisher TEXT,
            pages VARCHAR(20),
            description TEXT
        )
        """
        cursor.execute(query)

    @staticmethod
    @allure.step("Creating a User Table(user_table)")
    def create_user_table(cursor):
        """Create a User table (if is not exist)"""
        query = """
        CREATE TABLE IF NOT EXISTS user_table (
            id SERIAL PRIMARY KEY,
            userId TEXT UNIQUE,
            username TEXT,
            password TEXT,
            token TEXT,
            expires TIMESTAMP,
            created_date TIMESTAMP,
            isActive BOOL
        )
        """
        cursor.execute(query)

    @staticmethod
    @allure.step("Checking exists a Books Table(items_app)")
    def books_table_exist(cursor):
        cursor.execute("""
                    SELECT EXISTS(
                    SELECT FROM information_schema.tables
                    WHERE table_name = 'items_app'
                    )
        """)
        return cursor.fetchone()[0]

    @staticmethod
    @allure.step("Checking exists a User Table(user_table)")
    def user_table_exist(cursor):
        with cursor.connection.cursor() as cursor:
            cursor.execute("""
                        SELECT EXISTS(
                        SELECT FROM information_schema.tables
                        WHERE table_name = 'user_table'
                        )
            """)
            return cursor.fetchone()[0]

    @staticmethod
    @allure.step("Inserting user data into User Table(user_table)")
    def insert_user(cursor, user_data):
        cursor.execute("SELECT COUNT(*) FROM user_table WHERE userId = %s", (user_data["userId"],))
        exists = cursor.fetchone()[0]

        if exists:
            print(f"[INFO]User with {user_data['username']} already exists.")
            return

        query = """
        INSERT INTO user_table (userId, username, password, token, expires, created_date, isActive)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (userId) 
        DO UPDATE SET 
            username = EXCLUDED.username,
            password = EXCLUDED.password,
            token = EXCLUDED.token,
            expires = EXCLUDED.expires,
            created_date = EXCLUDED.created_date,
            isActive = EXCLUDED.isActive
        """
        values = (
            user_data["userId"], user_data["username"], user_data["password"],
            user_data["token"], user_data["expires"], user_data["created_date"],
            user_data["isActive"]
        )
        cursor.execute(query, values)

    @staticmethod
    @allure.step("Clear User Table(user_table)")
    def clear_user_table(cursor):
        """Clear Table"""
        cursor.execute("DELETE FROM user_table")

    @staticmethod
    @allure.step("Clear Books Table(items_app)")
    def clear_user_table(cursor):
        """Clear Table"""
        cursor.execute("DELETE FROM items_app")
