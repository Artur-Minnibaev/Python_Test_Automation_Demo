from datetime import datetime
import allure
import pytest
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
import config.config
import requests
from services.account.api_account import AccountAPI
import os
from dotenv import load_dotenv, set_key, dotenv_values
from services.db.database import PostgreSQL
import psycopg2
from services.db.configuration import DB_CONFIG
import time
import json
from services.db.parser import log_in

HOST = config.config.HOST


# @pytest.fixture(scope="session", autouse=True)
# def browser():
#     """Set up Chrome through Selenium Grid"""
#     chrome_options = webdriver.ChromeOptions()
#     # chrome_options.add_argument('--headless=new')
#     chrome_options.set_capability("browserName", "chrome")
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument('--disable-features=NetworkService')
#
#     max_attempts = 10
#     for attempt in range(max_attempts):
#         try:
#             driver = webdriver.Remote(
#                 command_executor='http://selenium-hub:4444/wd/hub',
#                 options=chrome_options,
#             )
#             driver.set_page_load_timeout(120)
#             driver.set_script_timeout(120)
#             print("[INFO] Selenium Grid is ready!")
#             break
#         except Exception as e:
#             print(f"[WARNING] Selenium Grid still not ready. Attempt {attempt+1}/{max_attempts}")
#             time.sleep(5)
#     else:
#         pytest.exit("[FAIL] Unsuccessful connection to Selenium Grid!")
#
#     yield driver
#
#     attach = driver.get_screenshot_as_png()
#     allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
#
#     driver.quit()

# @pytest.fixture(scope="session", autouse=True)
# def browser():
#     service = Service("/usr/local/bin/chromedriver")
#     options = webdriver.ChromeOptions()
#     options.add_argument("--no-proxy-server")
#     options.add_argument("--start-maximized")
#     # options.add_argument("--headless")
#     driver = webdriver.Chrome(service=service, options=options)
#     yield driver
#     attach = driver.get_screenshot_as_png()
#     allure.attach(attach, name=f"Screenshot {datetime.today}", attachment_type=allure.attachment_type.PNG)
#     driver.quit()


# Additionally generator for local testing
@pytest.fixture(scope="session", autouse=True)
def chrome_browser():
    chromedriver_path = chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    try:
        attach = driver.get_screenshot_as_png()
        allure.attach(
            attach,
            name=f"Screenshot {datetime.today().strftime('%Y-%m-%d_%H-%M-%S')}",
            attachment_type=allure.attachment_type.PNG
        )
    except Exception as e:
        print(f"[FAIL]Attempt creating screenshot: {e}")

    driver.quit()


@pytest.fixture(scope="session")
def wait_for_db():
    """Wait, 'till BD up"""
    for _ in range(2):
        try:
            conn = psycopg2.connect(
                host="main-postgres", user="postgres",
                password="postgres", dbname="test_db", port=5432
            )
            conn.close()
            print("[INFO] Database is ready!")
            return
        except psycopg2.OperationalError as e:
            print(f"[INFO] Waiting for database..., {e}")
            time.sleep(3)
    pytest.exit("[FAIL] Database did not start!")


@pytest.fixture(scope="function")
def set_up_db(wait_for_db):
    connection = psycopg2.connect(**DB_CONFIG)
    connection.autocommit = True
    cursor = connection.cursor()

    PostgreSQL.create_book_table(cursor)
    PostgreSQL.create_user_table(cursor)

    yield cursor
    cursor.close()
    connection.close()
    print("[INFO]Connection to the BD was closed")


@pytest.fixture(scope="session")
def api_data():
    log_in()
    with open("file.json", "r") as f:
        return json.load(f)["books"]
