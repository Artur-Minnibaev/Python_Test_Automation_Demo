import random
import time
import allure
from pages.elements_page import TextBoxPage
from pages.elements_page import CheckBoxPage
from pages.elements_page import RadioButtonPage
from pages.elements_page import WebTablePage
from conftest import browser

@allure.suite("Elements")
class TestElements:

    @allure.feature('TextBox')
    class TestTextBox:

        @allure.title('Check TextBox')
        def test_text_box(self, browser):
            # Test-case compares the data between input data and output data
            text_box_page = TextBoxPage(browser)
            text_box_page.open_page_text_box()
            text_box_page.remove_extra_elements()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data, "[FAIL] The data does not the same"

    @allure.feature('CheckBox')
    class TestCheckBox:

        @allure.title('Test of comparison input data and output data results using toggle dropdown list')
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

        @allure.title('Test of comparison input data and output data results using toggle dropdown list')
        def test_dropdown_list_using_expand_all_button(self, browser):
            # Test of comparison input data and output data results using toggle dropdown list
            browser.refresh()
            checkbox_page = CheckBoxPage(browser)
            checkbox_page.open_page_checkbox()
            checkbox_page.open_full_list_with_expand_all_button()
            checkbox_page.select_particular_element()
            input_result = checkbox_page.get_checked_box()
            output_result = checkbox_page.get_output_result()
            assert input_result == output_result, "[FAIL] The data does not the same"

        @allure.title('Test of verification randomly elements')
        def test_of_selected_randomly_elements(self, browser):
            # Test of verification randomly elements
            browser.refresh()
            checkbox_page = CheckBoxPage(browser)
            checkbox_page.open_full_list_with_expand_all_button()
            checkbox_page.select_random_elements()
            input_result = checkbox_page.get_checked_box()
            output_result = checkbox_page.get_output_result()
            assert input_result == output_result, "[FAIL] The data does not the same"

        @allure.title('Test of verification elements chosen by title')
        def test_of_selected_elements_by_title(self, browser):
            # Test of verification elements chosen by title
            browser.refresh()
            checkbox_page = CheckBoxPage(browser)
            checkbox_page.open_full_list_with_expand_all_button()
            checkbox_page.select_elements_by_title()
            input_result = checkbox_page.get_checked_box()
            output_result = checkbox_page.get_output_result()
            assert input_result == output_result, "[FAIL] The data does not the same"

        @allure.title('Test of verification elements with a closed dropdown list')
        def test_of_closing_dropdown_list_saving_output_data(self, browser):
            # Test of verification elements with a closed dropdown list
            checkbox_page = CheckBoxPage(browser)
            input_result = checkbox_page.get_checked_box()
            checkbox_page.collapse_all_button()
            output_result = checkbox_page.get_output_result()
            assert input_result == output_result, "[FAIL] The data does not the same"

    @allure.feature('RadioButton')
    class TestRadioButton:

        @allure.title('Check RadioButton')
        def test_radio_button(self, browser):
            # Test of selection options on the page "Radio Button"
            radio_button_page = RadioButtonPage(browser)
            radio_button_page.open_page_radio_button()
            radio_button_page.click_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' option has not been selected"
            assert output_impressive == 'Impressive', "'Impressive' option has not been selected"
            assert output_no == 'No', "'No' option has not been selected"

    @allure.feature('WebTable')
    class TestWebTable:

        @allure.title('Test of adding a person by clicking the "Submit" button')
        def test_add_person(self, browser):
            # Test of adding a person by clicking the "Submit" button
            web_table_page = WebTablePage(browser)
            web_table_page.open_page_web_table()
            input_data = web_table_page.add_new_person()
            web_table_page.submit_button()
            output_data = web_table_page.check_added_new_person()

            time.sleep(5)

            assert input_data in output_data, "[FAIL]Data is empty"

        @allure.title('Test of adding a person without clicking the "Submit" button')
        def test_closing_pop_up(self, browser):
            # Test of adding a person without clicking the "Submit" button
            web_table_page = WebTablePage(browser)
            web_table_page.open_page_web_table()
            input_data = web_table_page.add_new_person()
            web_table_page.close_pop_up()
            output_data = web_table_page.check_added_new_person()
            assert input_data not in output_data, "[FAIL]Data exists"

        @allure.title('Test of searching a person after its adding')
        def test_searching_person_in_the_table(self, browser):
            # Test of searching a person after it's adding
            web_table_page = WebTablePage(browser)
            web_table_page.open_page_web_table()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.submit_button()
            web_table_page.search_person(key_word)
            output_result = web_table_page.check_existing_person()
            assert key_word in output_result, "[FAIL]Person does not exist"

        @allure.title('Test of updating random information of person')
        def test_update_information_of_person(self, browser):
            # Test of updating an information of person
            web_table_page = WebTablePage(browser)
            web_table_page.open_page_web_table()
            key_word = web_table_page.add_new_person()[0]
            web_table_page.submit_button()
            web_table_page.search_person(key_word)
            web_table_page.edit_button()
            new_value = web_table_page.update_person_info()
            web_table_page.submit_button()
            assert new_value is not None, "Updated value is None"

            time.sleep(5)

            web_table_page.search_person(new_value)
            output_result = web_table_page.check_existing_person()
            assert new_value in output_result, "[FAIL]Updated info does not exist"

        def test_of_deleting_person(self, browser):
            web_table_page = WebTablePage(browser)
            web_table_page.open_page_web_table()
            key_word = web_table_page.add_new_person()[0]
            web_table_page.submit_button()
            web_table_page.search_person(key_word)
            web_table_page.delete_button()
            output_result = web_table_page.search_person(key_word)
            check_deleted = web_table_page.check_deleted()
            assert output_result is None, "[FAIL]Person still exists"
            assert check_deleted == "No rows found", "[FAIL]Person still exists"

        def test_web_table_change_count_row(self, browser):
            web_table_page = WebTablePage(browser)
            web_table_page.open_page_web_table()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], "[FAIL]The number of rows does not change"
