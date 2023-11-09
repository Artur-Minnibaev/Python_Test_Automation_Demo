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


class CheckBoxPageLocators:
    """Description of using locators"""
    LOCATORS_TOGGLE_DROPDOWN = (By.CSS_SELECTOR, "button[title='Toggle']")
    LOCATORS_TOGGLE_EXPAND_LIST = (By.CSS_SELECTOR, "button[title='Expand all']")
    LOCATORS_TOGGLE_COLLAPSE_LIST = (By.CSS_SELECTOR, "button[title='Collapse all']")
    LOCATORS_ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    LOCATORS_CHECKED_LIST = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-expand-close']")
    # LOCATORS_CHECKED_LIST = ".//ancestor::span[@class='rct-text']"
    LOCATORS_CHECKED_BOX = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
