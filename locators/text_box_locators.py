from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    """Description of using locators"""
    LOCATORS_FULL_NAME_FIELD = (By.CSS_SELECTOR, "input[id='userName']")
    LOCATORS_EMAIL_FIELD = (By.CSS_SELECTOR, "input[id='userEmail']")
    LOCATORS_CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    LOCATORS_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    LOCATORS_BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    CREATED_LOCATORS_FULL_NAME_FIELD = (By.CSS_SELECTOR, "#output #name")
    CREATED_LOCATORS_EMAIL_FIELD = (By.CSS_SELECTOR, "#output #email")
    CREATED_LOCATORS_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_LOCATORS_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")
