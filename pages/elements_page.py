import base64
import os
import random
import time

import allure
import requests
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By

from generator.genereator import generated_person, generated_file
from locators.elemets_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step("Fill in all fields")
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        with allure.step('filling fields'):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step('click submit button'):
            self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        i = 0
        while i <= random.randint(10, 20):
            item = item_list[random.randint(1, 15)]
            self.go_to_element(item)
            item.click()
            i = i + 1

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element('xpath', self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_BUTTON,
                   'impressive': self.locators.IMPRESSIVE_BUTTON,
                   'no': self.locators.NO_BUTTON}

        self.element_is_visible(choices[choice]).click()

    def get_output_text(self):
        date = self.element_is_visible(self.locators.OUTPUT_RESULT)
        return str(date.text)


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_persons(self):
        count = 4
        data = []
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(firstname)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.AGE).send_keys(age)
            self.element_is_visible(self.locators.SALARY).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

            count -= 1
            data.append([firstname, lastname, str(age), email, str(salary), department])
        return data

    def table_result(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_searched_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
        return row.text.splitlines()

    def edit_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        self.element_is_visible(self.locators.AGE).clear()
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    def delete_all_persons(self):
        persons = self.elements_are_visible(self.locators.DELETE_BUTTON)
        for item in persons:
            self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_that_table_is_empty(self):
        no_rows_found = self.element_is_visible(self.locators.EMPTY_TABLE)
        return str(no_rows_found.text)

    def switch_number_of_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            try:
                count_row_button = self.element_is_present(self.locators.ROW_COUNT)
                self.go_to_element(count_row_button)
                count_row_button.click()
                self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
                data.append(self.check_rows_count())
            except ElementClickInterceptedException:
                data.append(f"cant find {x} row selector")
        return data

    def check_rows_count(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def check_double_click(self):
        button = self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON)
        self.action_double_click(button)
        data = self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON_MESSAGE).text
        return str(data)

    def check_right_click(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
        data = self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON_MESSAGE).text
        return str(data)

    def check_click(self):
        self.element_is_visible(self.locators.CLICK_BUTTON).click()
        data = self.element_is_visible(self.locators.CLICK_BUTTON_MESSAGE).text
        return str(data)


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(simple_link.get_attribute('href'))
        if request.status_code == 200:
            simple_link.click()
            self.switch_to_new_tab()
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def check_broken_link(self):
        url = "https://demoqa.com/bad-request"
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code


class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    def upload_file(self):
        filepath = generated_file()
        self.element_is_visible(self.locators.UPLOAD_FILE_INPUT).send_keys(filepath)
        os.remove(filepath)
        text = self.element_is_visible(self.locators.UPLOADED_FILEPATH).text
        file_name = filepath.split('\\')[-1]
        result = text.split('\\')[-1]
        return file_name, result

    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_BUTTON).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf"C:\PythonProjects\WebAutomationFramework\testfile{random.randint(0, 999)}.jpg"
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    def check_changed_of_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property("color")
        time.sleep(5)
        color_button_after = color_button.value_of_css_property("color")
        return color_button_before, color_button_after

    def check_appear_of_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON, 6)
        except TimeoutException:
            return False
        return True

    def check_enable_after_button(self):
        try:
            self.element_is_clickable(self.locators.WILL_ENABLE_FIVE_SEC_BUTTON, 6)
        except TimeoutException:
            return False
        return True
