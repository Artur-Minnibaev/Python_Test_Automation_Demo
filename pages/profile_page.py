from pages.base_page import BasePage
from locators.profile_locators import ProfilePageLocators as locator


class ProfilePage(BasePage):

    def click_log_out_button(self):
        return self.element_is_visible(locator.LOCATOR_LOG_OUT_BUTTON).click()

    def check_main_header(self):
        return self.element_is_visible(locator.LOCATOR_MAIN_HEADER)
