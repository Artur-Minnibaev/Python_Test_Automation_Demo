from datetime import datetime
import allure
import pytest
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
import config.config
from services.db.database import PostgreSQL
import psycopg2
from services.db.configuration import DB_CONFIG
import time
import json
from services.db.parser import log_in

HOST = config.config.HOST


def pytest_addoption(parser):
    run_mode = parser.addoption("--run-mode", action="store", default="local", help="Choose run mode: local or docker")
    print(f"[DEBUG] Run mode is {run_mode}")


@pytest.fixture(scope="session")
def docker_browser():
    """Set up Chrome through Selenium Grid"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless=new')
    chrome_options.set_capability("browserName", "chrome")
    chrome_options.add_argument('--no-sandbox')

    max_attempts = 2
    for attempt in range(max_attempts):
        try:
            driver = webdriver.Remote(
                command_executor='http://selenium-hub:4444/wd/hub',
                options=chrome_options,
            )
            driver.set_page_load_timeout(120)
            driver.set_script_timeout(120)
            print("[INFO] Selenium Grid is ready!")
            break
        except Exception as e:
            print(f"[WARNING] Selenium Grid still not ready. Attempt {attempt+1}/{max_attempts}")
            time.sleep(5)
    else:
        pytest.exit("[FAIL] Unsuccessful connection to Selenium Grid!")

    yield driver

    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)

    driver.quit()


@pytest.fixture(scope="session")
def local_browser():
    """Local testing"""
    chromedriver_path = chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

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
        print(f"[FAIL] Exception during creating a screenshot: {e}")

    driver.quit()


@pytest.fixture(scope="session")
def browser(request):
    run_mode = request.config.getoption("--run-mode")
    print(f"[DEBUG] Running in mode: {run_mode}")

    if run_mode == "docker":
        return request.getfixturevalue("docker_browser")
    return request.getfixturevalue("local_browser")


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
