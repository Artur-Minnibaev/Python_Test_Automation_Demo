from pages.login_page import Login
from config import config

EXPECTED_TEXT = config.user_name


class TestLoginPage:

    def test_login(self, browser):
        start_page = Login(browser)
        start_page.go_to_site()
        start_page.remove_extra_elements()
        start_page.enter_username()
        start_page.enter_password()
        start_page.click_login_button()
        app_logo = ''
        for main_title in start_page.check_title():
            app_logo = main_title.text
        assert app_logo == EXPECTED_TEXT, "invalid title"
        assert browser.current_url != browser, "invalid url"
        print(f"{browser.current_url}")
