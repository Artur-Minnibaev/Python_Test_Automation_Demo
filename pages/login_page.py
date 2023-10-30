from pages.base_page import BasePage
from config import config
from locators.login_page_locators import LoginLocators


class Login(BasePage):
    """The function of LOG IN and check successful login system"""
    def enter_username(self):
        username_field = self.find_element(LoginLocators.LOCATOR_USERNAME_FIELD)
        username_field.send_keys(config.user_name)
        return username_field

    def enter_password(self):
        password_field = self.find_element(LoginLocators.LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(config.pass_word)
        return password_field

    def click_login_button(self):
        return self.element_is_visible(LoginLocators.LOCATOR_BUTTON_LOGIN).click()

    def check_title(self):
        return self.find_elements(LoginLocators.LOCATOR_APP_LOGO, time=5)
