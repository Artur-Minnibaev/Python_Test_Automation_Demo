from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session", autouse=True)
def browser():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--start-maximized")
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today}", attachment_type=allure.attachment_type.PNG)
    driver.quit()

# @pytest.fixture(scope="session", autouse=True)
# def browser():
#     # Note: Please specify your chromedriver local path here:
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Remote('http://localhost:4444/wd/hub', options=options)
#     yield driver
#     attach = driver.get_screenshot_as_png()
#     allure.attach(attach, name=f"Screenshot {datetime.today}", attachment_type=allure.attachment_type.PNG)
#     driver.quit()



