from datetime import datetime
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import config.config

HOST = config.config.HOST


@pytest.fixture(scope="session", autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable - blink - features = AutomationControlled')
    # Note: Please specify your chromedriver local path here:
    driver = webdriver.Remote(
        command_executor='http://chrome:4444/wd/hub',
        options=chrome_options,
    )
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today}", attachment_type=allure.attachment_type.PNG)
    driver.quit()


# Additionally generator for local testing
# @pytest.fixture(scope="session", autouse=True)
def browser_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today}", attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture(scope="session")
def get_Access_Token(requests=None):
    response = requests.post(
        url=f"{HOST}/GenerateToken", json={"Content-type": "application/json",
                                           "userName": config.config.user_name,
                                           "password": config.config.pass_word
                                           }
    )
    token = response.json()["token"]
    contents = []

    with open(".env", "r") as file:
        lines = file.read().splitlines()
        contents = lines[:-2]

    with open(".env", "w+") as file:
        contents.append(f'API_TOKEN={token}')
        file.write(contents[0])

    assert response.status_code == 200
    return response.json()['token']
