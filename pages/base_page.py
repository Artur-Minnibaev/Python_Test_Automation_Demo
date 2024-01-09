from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import config


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url_login = config.url_login
        self.base_url_profile = config.url_profile
        self.base_url_text_box = config.url_text_box
        self.base_url_checkbox = config.url_checkbox
        self.base_url_radio_button = config.url_radio_button
        self.base_url_web_table = config.url_web_table

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def element_is_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                                         message=f"Element is empty {locator}")

    def elements_are_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator),
                                                         message=f"Elements are empty {locator}")

    def element_is_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Element is empty {locator}")

    def elements_are_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Elements are empty {locator}")

    def element_is_not_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator),
                                                         message=f"Element is not visible {locator}")

    def element_is_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator),
                                                         message=f"Element is not clickable {locator}")

    def remove_extra_elements(self):
        self.driver.execute_script("document.getElementsByTagName('div')[4].remove();")
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').style.display='none';")

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def open_page_login(self):
        return self.driver.get(self.base_url_login)

    def open_page_profile(self):
        return self.driver.get(self.base_url_profile)

    def open_page_text_box(self):
        return self.driver.get(self.base_url_text_box)

    def open_page_checkbox(self):
        return self.driver.get(self.base_url_checkbox)

    def open_page_radio_button(self):
        return self.driver.get(self.base_url_radio_button)

    def open_page_web_table(self):
        return self.driver.get(self.base_url_web_table)
