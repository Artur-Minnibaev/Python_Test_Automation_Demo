import allure

from pages.base_page import BasePage
from config import config
from locators.login_page_locators import LoginPageLocators as locator


class LoginPage(BasePage):
    """The function of LOG IN and check successful login system"""
    @allure.step("Filling an username")
    def enter_username(self):
        username_field = self.find_element(locator.LOCATOR_USERNAME_FIELD)
        username_field.send_keys(config.user_name)
        return username_field

    @allure.step("Filling a password")
    def enter_password(self):
        password_field = self.find_element(locator.LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(config.pass_word)
        return password_field

    @allure.step("Click on the login button")
    def click_login_button(self):
        button = self.element_is_visible(locator.LOCATOR_BUTTON_LOGIN)
        self.scroll_to_element(button)
        self.element_is_clickable(locator.LOCATOR_BUTTON_LOGIN).click()

    @allure.step("Check title")
    def check_title(self):
        return self.find_elements(locator.LOCATOR_APP_LOGO)

    @allure.step("Check main header")
    def check_main_header(self):
        return self.find_element(locator.LOCATOR_MAIN_HEADER)
