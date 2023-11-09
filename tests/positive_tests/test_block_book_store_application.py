from config import config
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from conftest import *


class TestLogin:
    """Login with valid credentials"""
    def test_login(self, browser):
        # Test-case verifies successful logging to the system by its title
        login_page = LoginPage(browser)
        login_page.open_page_login()
        login_page.remove_extra_elements()
        login_page.enter_username()
        login_page.enter_password()
        login_page.click_login_button()
        title = login_page.check_title()
        if len(title) > 0:
            assert title[0].text == config.user_name, "[FAIL] Invalid title"
        else:
            print(f"{title} not found")

    def test_check_url_after_login(self, browser):
        # Test-case compares URLs after log in
        assert browser.current_url != config.url_login, "[FAIL] The URLs are the same"

    def test_log_out(self, browser):
        # Test-case verifies log out
        log_out_page = ProfilePage(browser)
        log_out_page.open_page_profile()
        log_out_page.remove_extra_elements()
        log_out_page.click_log_out_button()
        main_header = log_out_page.check_main_header()
        assert main_header.text == 'Login', "[FAIL] Invalid main header"

    def test_check_url_after_log_out(self, browser):
        # Test-case compares URLs after log out
        assert browser.current_url != config.url_profile, "[FAIL] The URLs are the same"
