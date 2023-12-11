from pages.widget_page import AccordianPage, AutocompletePage, DatePickerPage, SliderPage, ProgressBarPage


class TestWidgets:
    class TestAccordian:

        def test_first_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            title, content = accordian_page.check_accordian_by_index(1)
            assert title == "What is Lorem Ipsum?" and len(content) > 0, "Accordion is not present or not open"

        def test_second_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            title, content = accordian_page.check_accordian_by_index(2)
            assert title == "Where does it come from?" and len(content) > 0, "Accordion is not present or not open"

        def test_third_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            title, content = accordian_page.check_accordian_by_index(3)
            assert title == "Why do we use it?" and len(content) > 0, "Accordion is not present or not open"

        def test_accordian_one_by_one(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian_by_index(1)
            assert first_title == "What is Lorem Ipsum?" and len(first_content) > 0, \
                "Accordion is not present or not open"
            second_title, second_content = accordian_page.check_accordian_by_index(2)
            assert second_title == "Where does it come from?" and len(second_content) > 0, \
                "Accordion is not present or not open"
            third_title, third_content = accordian_page.check_accordian_by_index(3)
            assert third_title == "Why do we use it?" and len(third_content) > 0, \
                "Accordion is not present or not open"

    class TestAutocomplete:

        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi_with_random_colors()
            colors_result = autocomplete_page.check_color_in_multy()
            assert colors == colors_result, "The Multiple Autocomplete isn't filled, or content was different"

        def test_remove_element_from_multi_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            autocomplete_page.fill_input_multi_with_random_colors()
            value_before, value_after = autocomplete_page.remove_one_value_form_multy()
            assert value_before == value_after + 1, "The element from Multiple Autocomplete isn't deleted"

        def test_single_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single_with_random_color()
            output = autocomplete_page.check_color_in_single()
            assert color == output, "The Single Autocomplete isn't filled, or content was different"

    class TestDatePicker:

        def test_select_date(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            old, new = date_picker_page.set_date()
            assert old != new, "The date picker is not editable"

        def test_select_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            old, new = date_picker_page.set_date_and_time()
            assert old != new, "The date picker is not editable"

    class TestSlider:

        def test_slider(self, driver):
            slider_page = SliderPage(driver, "https://demoqa.com/slider")
            slider_page.open()
            before, after = slider_page.change_slider_value()
            assert before != after, "The value of the slider has not been changed"

    class TestProgressBarPage:

        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar.open()
            before, after = progress_bar.change_progress_bar_value()
            assert before != after, "The value of the progress bar has not been changed"

