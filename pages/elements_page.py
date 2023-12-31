import random
from pages.base_page import BasePage
from locators.elements_page_locators import *
from generator.generator import generated_person


class TextBoxPage(BasePage):

    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        """Filling all fields on the Text Box page"""
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address.replace("\n", " ")
        permanent_address = person_info.permanent_address.replace("\n", " ")
        self.element_is_visible(self.locators.LOCATOR_FULL_NAME_FIELD).send_keys(full_name)
        self.element_is_visible(self.locators.LOCATOR_EMAIL_FIELD).send_keys(email)
        self.element_is_visible(self.locators.LOCATOR_CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.LOCATOR_PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.LOCATOR_BUTTON_SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        """Obtaining selected data on the Text Box page"""
        full_name = self.element_is_present(self.locators.CREATED_LOCATOR_FULL_NAME_FIELD).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_LOCATOR_EMAIL_FIELD).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_LOCATOR_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_LOCATOR_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):

    locator = CheckBoxPageLocators()

    def open_full_list_with_toggle_dropdown_button(self):
        """Expanding all elements by clicking on the toggles"""
        self.element_is_present(self.locator.LOCATOR_TOGGLE_DROPDOWN).click()
        while True:
            toggle_list1 = self.elements_are_present(self.locator.LOCATOR_CHECKED_LIST)
            for toggle1 in toggle_list1:
                self.go_to_element(toggle1)
                toggle1.click()
            toggle_list2 = self.elements_are_present(self.locator.LOCATOR_CHECKED_LIST)
            for toggle2 in toggle_list2:
                self.go_to_element(toggle2)
                toggle2.click()
            else:
                break

    def open_full_list_with_expand_all_button(self):
        """Expanding all elements by clicking on a 'Expand button'"""
        self.element_is_visible(self.locator.LOCATOR_TOGGLE_EXPAND_LIST).click()

    def collapse_all_button(self):
        """Closing all elements by clicking on a 'Collapse button'"""
        self.element_is_visible(self.locator.LOCATOR_TOGGLE_COLLAPSE_LIST).click()

    def select_elements_by_title(self):
        """Selecting elements by title"""
        item_list = self.elements_are_visible(self.locator.LOCATOR_ITEM_LIST)
        for item in item_list:
            self.go_to_element(item)
            item.click()

    def select_particular_element(self):
        """Selecting a particular element"""
        elements_list = self.elements_are_visible(self.locator.LOCATOR_CHECKED_BOX)
        element = elements_list[random.randint(1, 16)]
        self.go_to_element(element)
        element.click()

    def select_random_elements(self):
        """Selecting random elements"""
        item_list = self.elements_are_visible(self.locator.LOCATOR_ITEM_LIST)
        count = 17
        while count != 0:
            item = item_list[random.randint(1, 16)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_box(self):
        """Jump to elements"""
        checked_list = self.elements_are_present(self.locator.LOCATOR_CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locator.LOCATOR_TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('.doc', '').lower()

    def get_output_result(self):
        """Obtaining output results"""
        result_list = self.elements_are_present(self.locator.LOCATOR_OUTPUT_ITEMS_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):

    locator = RadioButtonPageLocators()

    def click_radio_button(self, choice):
        choices = {
            'yes': self.locator.LOCATOR_YES_RADIOBUTTON,
            'impressive': self.locator.LOCATOR_IMPRESSIVE_RADIOBUTTON,
            'no': self.locator.LOCATOR_NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locator.LOCATOR_OUTPUT_RESULT).text
