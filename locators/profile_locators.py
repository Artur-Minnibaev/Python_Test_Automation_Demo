from selenium.webdriver.common.by import By


class ProfileLocators:
    """Description of using locators"""
    LOCATOR_LOG_OUT_BUTTON = (By.XPATH, "//button[text()='Log out']")
    LOCATOR_MAIN_HEADER = (By.XPATH, "//*[@class='main-header']")
