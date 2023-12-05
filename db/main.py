import psycopg2
from configuration import *
import json


class PostgreSQL:
    """Connecting, Creating, Inserting Data into the Table"""

    def __init__(self):

        self.connect = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

    def version_table(self):
        """Responding about a version of table"""
        with self.connect.cursor() as cursor:
            self.connect.autocommit = True
            cursor.execute(
                "SELECT version();"
            )
            print(f"Server version: {cursor.fetchone()}")

    def create_table(self):
        """Creating a table if not exists"""
        try:
            with self.connect.cursor() as cursor:
                self.connect.autocommit = True
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS items_app(
                id SERIAL PRIMARY KEY,
                isbn TEXT,
                title TEXT,
                subTitle TEXT,
                author TEXT,
                publish_date DATE,
                publisher TEXT,
                pages VARCHAR(20),
                description TEXT) """
                               )
                print("[INFO] Table is created successfully")
        except Exception as ex:
            print("[INFO] Error while working with PosgreSQL", ex)
        finally:
            if self.connect:
                self.connect.close()

    def insert_table(self):
        """Inserting Data from a parsing file"""
        try:
            with self.connect.cursor() as cursor:
                self.connect.autocommit = True
                with open('file.json', 'r') as f:
                    data = json.load(f)
                    for d in data["books"]:
                        new_data = ([{"isbn": d["isbn"], "title": d["title"], "subTitle": d["subTitle"], "author": d["author"],
                                      "publish_date": d["publish_date"], "publisher": d["publisher"], "pages": int(d["pages"]),
                                      "description": d["description"]}])
                        for item in new_data:
                            values = (item["isbn"], item["title"], item["subTitle"], item["author"], item["publish_date"],
                                      item["publisher"], item["pages"], item["description"])
                            pg_sql = "insert into items_app(isbn, title, subTitle, author, publish_date, publisher, " \
                                     "pages, description)" \
                                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                            cursor.execute(pg_sql, values)
                            print(cursor.rowcount, "Row(s) is/are inserted to the table successfully!")
        except Exception as ex:
            print("[INFO] Error while working with PosgreSQL", ex)
        finally:
            if self.connect:
                self.connect.close()
                print("[INFO] PostgreSQL connection is closed")


if __name__ == '__main__':
    PostgreSQL().__init__()
    PostgreSQL().version_table()
    PostgreSQL().create_table()
    PostgreSQL().insert_table()
