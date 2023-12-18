import os

from selenium.webdriver import Keys

from generator.genereator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_data(self):
        person_info = next(generated_person())
        file_path = generated_file()

        first_name = self.element_is_visible(self.locators.FIRST_NAME)
        last_name = self.element_is_visible(self.locators.LAST_NAME)
        email = self.element_is_visible(self.locators.EMAIL)
        gender = self.element_is_visible(self.locators.GENDER)
        mobile = self.element_is_visible(self.locators.MOBILE)
        subject = self.element_is_visible(self.locators.SUBJECT)
        hobbies = self.element_is_visible(self.locators.HOBBIES)
        file_input = self.element_is_visible(self.locators.FILE_INPUT)
        current_address = self.element_is_visible(self.locators.CURRENT_ADDRESS)
        self.remove_footer()
        submit = self.element_is_visible(self.locators.SUBMIT)

        firstname = person_info.firstname
        lastname = person_info.lastname
        email_data = person_info.email
        gender_data = gender.text
        phone_number = person_info.phone_number
        current_address_data = person_info.current_address

        first_name.send_keys(firstname)
        last_name.send_keys(lastname)
        email.send_keys(email_data)
        gender.click()
        mobile.send_keys(phone_number)
        subject.send_keys("English")
        subject.send_keys(Keys.RETURN)
        hobbies.click()
        file_input.send_keys(file_path)
        os.remove(file_path)
        current_address.send_keys(current_address_data)
        submit.click()

        data = [f"{firstname} {lastname}", email_data, gender_data, phone_number,
                current_address_data.replace("\n", " ")]
        return data[:4]

    def form_result(self):
        result_list = self.elements_are_visible(self.locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]
        return result_text[:4]
