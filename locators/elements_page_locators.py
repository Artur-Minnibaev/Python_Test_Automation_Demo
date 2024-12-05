from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    """Description of using locators"""
    LOCATOR_FULL_NAME_FIELD = (By.CSS_SELECTOR, "input[id='userName']")
    LOCATOR_EMAIL_FIELD = (By.CSS_SELECTOR, "input[id='userEmail']")
    LOCATOR_CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    LOCATOR_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    LOCATOR_BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    CREATED_LOCATOR_FULL_NAME_FIELD = (By.CSS_SELECTOR, "#output #name")
    CREATED_LOCATOR_EMAIL_FIELD = (By.CSS_SELECTOR, "#output #email")
    CREATED_LOCATOR_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_LOCATOR_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    """Description of using locators"""
    LOCATOR_TOGGLE_DROPDOWN = (By.CSS_SELECTOR, "button[title='Toggle']")
    LOCATOR_TOGGLE_EXPAND_LIST = (By.CSS_SELECTOR, "button[title='Expand all']")
    LOCATOR_TOGGLE_COLLAPSE_LIST = (By.CSS_SELECTOR, "button[title='Collapse all']")
    LOCATOR_ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    LOCATOR_CHECKED_LIST = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-expand-close']")
    LOCATOR_TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    LOCATOR_CHECKED_BOX = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-uncheck']")
    LOCATOR_CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    LOCATOR_OUTPUT_ITEMS_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    """Description of using locators"""
    LOCATOR_YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    LOCATOR_NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    LOCATOR_IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    LOCATOR_OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTablePageLocators:
    """Description of using locators"""
    # adding person
    LOCATOR_ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    LOCATOR_FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LOCATOR_LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    LOCATOR_EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    LOCATOR_AGE = (By.CSS_SELECTOR, "input[id='age']")
    LOCATOR_SALARY = (By.CSS_SELECTOR, "input[id='salary']")
    LOCATOR_DEPARTMENT = (By.CSS_SELECTOR, "input[id='department']")
    LOCATOR_SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")
    LOCATOR_CLOSE_BUTTON_POP_UP = (By.CSS_SELECTOR, "span[aria-hidden='true']")

    # searching person
    LOCATOR_FULL_PERSON_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    LOCATOR_SEARCH_FIELD = (By.CSS_SELECTOR, "input[id='searchBox']")
    LOCATOR_DELETE_PERSON = (By.CSS_SELECTOR, "span[title='Delete']")
    LOCATOR_ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    LOCATOR_COUNT_ROW_LISTS = (By.CSS_SELECTOR, "select[aria-label='rows per page']")

    # update information
    LOCATOR_UPDATE_PERSON = (By.CSS_SELECTOR, "span[title='Edit']")

    # delete person
    LOCATOR_DELETE_PERSON = (By.CSS_SELECTOR, "span[title='Delete']")
    LOCATOR_CHECK_DELETED = (By.CSS_SELECTOR, "div[class='rt-noData']")
