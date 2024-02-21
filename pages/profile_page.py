import allure

from pages.base_page import BasePage
from locators.profile_locators import ProfilePageLocators as locator


class ProfilePage(BasePage):

    @allure.step("Click on the logout button")
    def click_log_out_button(self):
        return self.element_is_visible(locator.LOCATOR_LOG_OUT_BUTTON).click()

    @allure.step("Check title")
    def check_main_header(self):
        return self.element_is_visible(locator.LOCATOR_MAIN_HEADER)
