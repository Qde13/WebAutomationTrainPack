import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address.replace('\n', ' ') == output_cur_addr, "the current address does not match"
            assert permanent_address.replace('\n', ' ') == output_per_addr, "the permanent address does not match"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(f"input: {input_checkbox}")
            print(f"output: {output_result}")
            assert input_checkbox == output_result, "checkboxes have not been selected"

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_text()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_text()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_text()
            assert output_yes == 'Yes', "Radio button is not clickable, or output is wrong"
            assert output_impressive == 'Impressive', "Radio button is not clickable, or output is wrong"
            assert output_no == "No", "Radio button is not clickable, or output is wrong"

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_persons = web_table_page.add_new_persons()  # add 4 new random persons to the table
            table_result = web_table_page.table_result()
            print(new_persons)
            print(table_result)
            for item in new_persons:
                assert item in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            random_key_word = web_table_page.add_new_persons()[random.randint(0, 3)][random.randint(0, 5)]
            web_table_page.search_some_person(random_key_word)
            table_result = web_table_page.check_searched_person()
            assert random_key_word in table_result, "The person was not found in the table"

        def test_web_table_edit_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            random_person = web_table_page.add_new_persons()[random.randint(0, 3)][random.randint(0, 5)]
            web_table_page.search_some_person(random_person)
            age = web_table_page.edit_person_info()
            row = web_table_page.check_searched_person()
            assert age in row
