from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Description of using locators"""
    LOCATOR_USERNAME_FIELD = (By.ID, "userName")  # //input[@id='userName']
    LOCATOR_PASSWORD_FIELD = (By.ID, "password")  # //input[@id='password']
    LOCATOR_BUTTON_LOGIN = (By.XPATH, "//*[@id='login']")  # //*[@id="login"]
    LOCATOR_APP_LOGO = (By.ID, "userName-value")  # //label[@id='userName-value']
    LOCATOR_MAIN_HEADER = (By.XPATH, "//label[contains(text(), 'You are already logged in. View your')]")

