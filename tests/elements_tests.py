import random
import time

import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


@allure.suite("Elements")
class TestElements:
    @allure.feature("TextBox")
    class TestTextBox:
        @allure.title("Checking Text Box")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address.replace('\n', ' ') == output_cur_addr, "the current address does not match"
            assert permanent_address.replace('\n', ' ') == output_per_addr, "the permanent address does not match"

    @allure.feature("Check Box")
    class TestCheckBox:
        @allure.title("Checking Check Box")
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

    @allure.feature("Radio Button")
    class TestRadioButton:
        @allure.title("Checking Radio Button")
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

    @allure.feature("Web Table")
    class TestWebTable:
        @allure.title("Checking Web table add 4 new random persons to the table")
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_persons = web_table_page.add_new_persons()
            table_result = web_table_page.table_result()
            print(new_persons)
            print(table_result)
            for item in new_persons:
                assert item in table_result

        @allure.title("Checking Web table search random person form added random persons")
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            random_key_word = web_table_page.add_new_persons()[random.randint(0, 3)][random.randint(0, 5)]
            web_table_page.search_some_person(random_key_word)
            table_result = web_table_page.check_searched_person()
            assert random_key_word in table_result, "The person was not found in the table"

        @allure.title("Checking Web table edit random person form added random persons")
        def test_web_table_edit_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            random_person = web_table_page.add_new_persons()[random.randint(0, 3)][random.randint(0, 5)]
            web_table_page.search_some_person(random_person)
            age = web_table_page.edit_person_info()
            row = web_table_page.check_searched_person()
            assert age in row, "The person card has not been changed"

        @allure.title("Checking Web table delete random person form added random persons")
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            random_person = web_table_page.add_new_persons()[random.randint(0, 3)][random.randint(0, 5)]
            web_table_page.search_some_person(random_person)
            web_table_page.delete_all_persons()
            time.sleep(5)
            no_rows_found = web_table_page.check_that_table_is_empty()
            assert no_rows_found == "No rows found", "The table is not empty"

        @allure.title("Checking Web table change row count functionality")
        def test_web_table_change_row_count(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.switch_number_of_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], 'The number of rows in the table has not been changed or has changed incorrectly'

    @allure.feature("Buttons")
    class TestButtons:
        @allure.title("Checking the double click button")
        def test_doubleclick_button(self, driver):
            buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            buttons_page.open()
            double_click = buttons_page.check_double_click()
            assert double_click == 'You have done a double click', "The double click was not pressed"

        @allure.title("Checking the right click button")
        def test_right_click_button(self, driver):
            buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            buttons_page.open()
            right_click = buttons_page.check_right_click()
            assert right_click == 'You have done a right click', "The right click was not pressed"

        @allure.title("Checking the dynamic click button")
        def test_click_button(self, driver):
            buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            buttons_page.open()
            click = buttons_page.check_click()
            assert click == 'You have done a dynamic click', "The dynamic click was not pressed"

    @allure.feature("Links")
    class TestLinks:
        @allure.title("Checking that link opens new browser window")
        def test_check_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "New window with link address isn't opened"

        @allure.title("Checking that link response 400 code")
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.check_broken_link()
            assert response_code == 400, "Link isn't broken"

    @allure.feature("Upload abd Download")
    class TestUploadAndDownload:
        @allure.title("Checking file upload")
        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
            upload_download_page.open()
            file_name, result_name = upload_download_page.upload_file()
            assert file_name == result_name, "The file has not been uploaded"

        @allure.title("Checking file download")
        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, "The file has not been downloaded"

    @allure.feature("Dynamic Properties")
    class TestDynamicProperties:
        @allure.title("Checking dynamic color button")
        def test_dynamic_color_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_of_color()
            assert color_before != color_after, "Colors button did not been changed"

        @allure.title("Checking dynamic appear button")
        def test_dynamic_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_of_button()
            assert appear is True, "Button did not appear after 5 sec"

        @allure.title("Checking dynamic enable button")
        def test_dynamic_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_after_button()
            assert enable is True, "Button did not enable after 5 sec"
