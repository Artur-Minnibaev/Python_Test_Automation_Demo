from pages.base_page import BasePage
from locators.text_box_locators import TextBoxPageLocators as locator
from generator.generator import generated_person


class TextBoxPage(BasePage):

    def fill_all_fields(self):
        """Filling all fields on the Text Box page"""
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address.replace("\n", " ")
        permanent_address = person_info.permanent_address.replace("\n", " ")
        self.element_is_visible(locator.LOCATORS_FULL_NAME_FIELD).send_keys(full_name)
        self.element_is_visible(locator.LOCATORS_EMAIL_FIELD).send_keys(email)
        self.element_is_visible(locator.LOCATORS_CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(locator.LOCATORS_PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(locator.LOCATORS_BUTTON_SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        """Obtaining data on the Text Box page"""
        full_name = self.element_is_present(locator.CREATED_LOCATORS_FULL_NAME_FIELD).text.split(':')[1]
        email = self.element_is_present(locator.CREATED_LOCATORS_EMAIL_FIELD).text.split(':')[1]
        current_address = self.element_is_present(locator.CREATED_LOCATORS_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(locator.CREATED_LOCATORS_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address
