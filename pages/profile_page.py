from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators


class ProfilePage(BasePage):

    def click_log_out_button(self):
        return self.element_is_visible(ProfileLocators.LOCATOR_LOG_OUT_BUTTON).click()

    def check_main_header(self):
        return self.element_is_visible(ProfileLocators.LOCATOR_MAIN_HEADER)
