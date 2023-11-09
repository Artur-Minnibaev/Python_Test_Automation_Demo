from pages.elements_page import TextBoxPage
from pages.elements_page import CheckBoxPage


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
            checkbox_page = CheckBoxPage(browser)
            checkbox_page.open_page_checkbox()
            checkbox_page.open_full_list_with_toggle_dropdown_button()

        def test_dropdown_list_with_expand_all_button(self, browser):
            pass

        def test_close_list_with_collapse_all_button(self, browser):
            pass

        def test_of_selected_all_elements(self, browser):
            pass

        def test_of_selected_random_elements(self, browser):
            pass
