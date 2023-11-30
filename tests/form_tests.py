from pages.form_page import FormPage


class TestForm:
    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        filled_data = form_page.fill_form_data()
        result_data = form_page.form_result()
        assert filled_data == result_data, "Form isn't filled or the result is different"
