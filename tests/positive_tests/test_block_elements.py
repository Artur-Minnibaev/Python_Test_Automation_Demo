import time
from pages.elements_page import TextBoxPage
from pages.elements_page import CheckBoxPage
from conftest import *


class TestElements:
    class TestTextBox:
        def test_text_box(self, browser):
            # Test-case compares the data between input data and output data
            text_box_page = TextBoxPage(browser)
            text_box_page.open_page_text_box()
            text_box_page.remove_extra_elements()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data, "[FAIL] The data does not the same"

    class TestCheckBox:

        def test_dropdown_list_using_toggle_dropdown_button(self, browser):
            # Test of comparison input data and output data results using toggle dropdown list
            checkbox_page = CheckBoxPage(browser)
            checkbox_page.open_page_checkbox()
            checkbox_page.open_full_list_with_toggle_dropdown_button()
            checkbox_page.select_particular_element()
            input_result = checkbox_page.get_checked_box()
            output_result = checkbox_page.get_output_result()
            assert input_result == output_result, "[FAIL] The data does not the same"
            # checkbox_page.collapse_all_button()

        def test_dropdown_list_using_expand_all_button(self, browser):
            # Test of comparison input data and output data results using toggle dropdown list
            browser.refresh()
            checkbox_page = CheckBoxPage(browser)
            checkbox_page.open_full_list_with_expand_all_button()
            checkbox_page.select_particular_element()
            input_result = checkbox_page.get_checked_box()
            output_result = checkbox_page.get_output_result()
            assert input_result == output_result, "[FAIL] The data does not the same"

        def test_of_selected_randomly_elements(self, browser):
            # Test of verification randomly elements
            browser.refresh()
            checkbox_page = CheckBoxPage(browser)
            checkbox_page.open_full_list_with_expand_all_button()
            checkbox_page.select_random_elements()
            input_result = checkbox_page.get_checked_box()
            output_result = checkbox_page.get_output_result()
            assert input_result == output_result, "[FAIL] The data does not the same"

        def test_of_selected_elements_by_title(self, browser):
            # Test of verification elements chosen by title
            browser.refresh()
            checkbox_page = CheckBoxPage(browser)
            checkbox_page.open_full_list_with_expand_all_button()
            checkbox_page.select_elements_by_title()
            input_result = checkbox_page.get_checked_box()
            output_result = checkbox_page.get_output_result()
            assert input_result == output_result, "[FAIL] The data does not the same"

        def test_of_closing_dropdown_list_saving_output_data(self, browser):
            # Test of verification elements with a closed dropdown list
            checkbox_page = CheckBoxPage(browser)
            input_result = checkbox_page.get_checked_box()
            checkbox_page.collapse_all_button()
            output_result = checkbox_page.get_output_result()
            assert input_result == output_result, "[FAIL] The data does not the same"
