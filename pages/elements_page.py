import random
import allure
from pages.base_page import BasePage
from locators.elements_page_locators import *
from generator.generator import generated_person


class TextBoxPage(BasePage):

    locators = TextBoxPageLocators()

    @allure.step("Filling in all fields")
    def fill_all_fields(self):
        """Filling all fields on the Text Box page"""
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address.replace("\n", " ")
        permanent_address = person_info.permanent_address.replace("\n", " ")
        with allure.step('filing fields'):
            self.element_is_visible(self.locators.LOCATOR_FULL_NAME_FIELD).send_keys(full_name)
            self.element_is_visible(self.locators.LOCATOR_EMAIL_FIELD).send_keys(email)
            self.element_is_visible(self.locators.LOCATOR_CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.LOCATOR_PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step('click on submit button'):
            self.element_is_visible(self.locators.LOCATOR_BUTTON_SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step("Check filled form")
    def check_filled_form(self):
        """Obtaining selected data on the Text Box page"""
        full_name = self.element_is_present(self.locators.CREATED_LOCATOR_FULL_NAME_FIELD).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_LOCATOR_EMAIL_FIELD).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_LOCATOR_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_LOCATOR_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):

    locator = CheckBoxPageLocators()

    @allure.step("Open full list")
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

    @allure.step("Open full list")
    def open_full_list_with_expand_all_button(self):
        """Expanding all elements by clicking on a 'Expand button'"""
        self.element_is_visible(self.locator.LOCATOR_TOGGLE_EXPAND_LIST).click()

    @allure.step("Close full list")
    def collapse_all_button(self):
        """Closing all elements by clicking on a 'Collapse button'"""
        self.element_is_visible(self.locator.LOCATOR_TOGGLE_COLLAPSE_LIST).click()

    @allure.step("Open list")
    def select_elements_by_title(self):
        """Selecting elements by title"""
        item_list = self.elements_are_visible(self.locator.LOCATOR_ITEM_LIST)
        for item in item_list:
            self.go_to_element(item)
            item.click()

    @allure.step("Open partially list")
    def select_particular_element(self):
        """Selecting a particular element"""
        elements_list = self.elements_are_visible(self.locator.LOCATOR_CHECKED_BOX)
        element = elements_list[random.randint(1, 16)]
        self.go_to_element(element)
        element.click()

    @allure.step("Click random items")
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

    @allure.step("Get checked checkbox")
    def get_checked_box(self):
        """Jump to elements"""
        checked_list = self.elements_are_present(self.locator.LOCATOR_CHECKED_ITEMS)
        data = []
        for box in checked_list:
            # find DOM-element using XPATH by method .//ancestor
            title_item = box.find_element(By.XPATH, self.locator.LOCATOR_TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('.doc', '').lower()

    @allure.step("Get output results")
    def get_output_result(self):
        """Obtaining output results"""
        result_list = self.elements_are_present(self.locator.LOCATOR_OUTPUT_ITEMS_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):

    locator = RadioButtonPageLocators()

    @allure.step("Click on the radiobutton")
    def click_radio_button(self, choice):
        """Choose options among radiobuttons"""
        choices = {
            'yes': self.locator.LOCATOR_YES_RADIOBUTTON,
            'impressive': self.locator.LOCATOR_IMPRESSIVE_RADIOBUTTON,
            'no': self.locator.LOCATOR_NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    @allure.step("Get output results")
    def get_output_result(self):
        """Obtaining output results"""
        return self.element_is_present(self.locator.LOCATOR_OUTPUT_RESULT).text


class WebTablePage(BasePage):

    locator = WebTablePageLocators()

    @allure.step("Add a new person")
    def add_new_person(self):
        """Adding a new person"""
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            with allure.step('open form of adding a new person'):
                self.element_is_visible(self.locator.LOCATOR_ADD_BUTTON).click()
            with allure.step('filling fields'):
                self.element_is_visible(self.locator.LOCATOR_FIRST_NAME).send_keys(firstname)
                self.element_is_visible(self.locator.LOCATOR_LAST_NAME).send_keys(lastname)
                self.element_is_visible(self.locator.LOCATOR_EMAIL).send_keys(email)
                self.element_is_visible(self.locator.LOCATOR_AGE).send_keys(age)
                self.element_is_visible(self.locator.LOCATOR_SALARY).send_keys(salary)
                self.element_is_visible(self.locator.LOCATOR_DEPARTMENT).send_keys(department)
            with allure.step('click on the submit button'):
                self.element_is_visible(self.locator.LOCATOR_SUBMIT).click()
            count -= 1
            return [firstname, lastname, str(age), email, str(salary), department]

    @allure.step("Checking an added person")
    def check_added_new_person(self):
        """Obtaining output results"""
        person_list = self.elements_are_present(self.locator.LOCATOR_FULL_PERSON_LIST)
        data = []
        for person in person_list:
            data.append(person.text.splitlines())
        return data

    @allure.step("Close pop-up")
    def close_pop_up(self):
        """Closing a pop-up without adding a new person to the list"""
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            with allure.step('open form of adding a new person'):
                self.element_is_visible(self.locator.LOCATOR_ADD_BUTTON).click()
            with allure.step('filling fields'):
                self.element_is_visible(self.locator.LOCATOR_FIRST_NAME).send_keys(firstname)
                self.element_is_visible(self.locator.LOCATOR_LAST_NAME).send_keys(lastname)
                self.element_is_visible(self.locator.LOCATOR_EMAIL).send_keys(email)
                self.element_is_visible(self.locator.LOCATOR_AGE).send_keys(age)
                self.element_is_visible(self.locator.LOCATOR_SALARY).send_keys(salary)
                self.element_is_visible(self.locator.LOCATOR_DEPARTMENT).send_keys(department)
            with allure.step('click on the submit button'):
                self.element_is_visible(self.locator.LOCATOR_CLOSE_BUTTON_POP_UP).click()
            count -= 1
            return [firstname, lastname, str(age), email, str(salary), department]
