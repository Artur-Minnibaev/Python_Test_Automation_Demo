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
        self.element_is_visible(self.locators.LOCATORS_FULL_NAME_FIELD).send_keys(full_name)
        self.element_is_visible(self.locators.LOCATORS_EMAIL_FIELD).send_keys(email)
        self.element_is_visible(self.locators.LOCATORS_CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.LOCATORS_PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.LOCATORS_BUTTON_SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        """Obtaining data on the Text Box page"""
        full_name = self.element_is_present(self.locators.CREATED_LOCATORS_FULL_NAME_FIELD).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_LOCATORS_EMAIL_FIELD).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_LOCATORS_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_LOCATORS_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):

    locator = CheckBoxPageLocators()

    def open_full_list_with_toggle_dropdown_button(self):
        self.element_is_present(self.locator.LOCATORS_TOGGLE_DROPDOWN).click()
        toggle_list = self.elements_are_present(self.locator.LOCATORS_CHECKED_LIST)
        for toggle in toggle_list:
            self.go_to_element(toggle)
            toggle.click()

    def open_full_list_with_expand_all_button(self):
        self.element_is_visible(self.locator.LOCATORS_TOGGLE_EXPAND_LIST).click()

    def collapse_all_button(self):
        self.element_is_visible(self.locator.LOCATORS_TOGGLE_COLLAPSE_LIST).click()

    def select_all_elements(self):
        self.element_is_visible(self.locator.LOCATORS_ITEM_LIST).click()

    def select_random_elements(self):
        item_list = self.element_is_visible(self.locator.LOCATORS_ITEM_LIST)
        item = item_list[random.randint(1, 17)]
        self.go_to_element(item).click()

    def compare_toggle_list(self):
        toggle_list = self.elements_are_present(self.locator.LOCATORS_CHECKED_LIST)
        return toggle_list

    def get_checked_box(self):
        pass
