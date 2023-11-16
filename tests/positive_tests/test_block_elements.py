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

        def test_dropdown_list_wit_toggle_dropdown_button(self, browser):
            # Test of compare checked checkboxes
            checkbox_page = CheckBoxPage(browser)
            checkbox_page.open_page_checkbox()
            checkbox_page.open_full_list_with_toggle_dropdown_button()
            checkbox_page.select_particular_element()
            checkbox_page.get_checked_box()
            input_result = checkbox_page.get_checked_box()
            output_result = checkbox_page.get_output_result()
            assert input_result == output_result, "[FAIL] The data does not the same"

        def test_dropdown_list_with_expand_all_button(self, browser):
            pass

        def test_close_list_with_collapse_all_button(self, browser):
            pass

        def test_of_selected_all_elements(self, browser):
            pass

        def test_of_selected_random_elements(self, browser):
            pass
