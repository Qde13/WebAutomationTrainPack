import allure
from selenium.common import TimeoutException

from pages.widget_page import AccordianPage, AutocompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


@allure.suite("Widget page tests")
class TestWidgets:
    @allure.feature("Accordian")
    class TestAccordian:
        @allure.title("Verify that the accordian is present and contains content")
        def test_first_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            title, content = accordian_page.check_accordian_by_index(1)
            assert title == "What is Lorem Ipsum?" and len(content) > 0, "Accordion is not present or not open"

        @allure.title("Verify that the accordian is present and contains content")
        def test_second_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            title, content = accordian_page.check_accordian_by_index(2)
            assert title == "Where does it come from?" and len(content) > 0, "Accordion is not present or not open"

        @allure.title("Verify that the accordian is present and contains content")
        def test_third_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            title, content = accordian_page.check_accordian_by_index(3)
            assert title == "Why do we use it?" and len(content) > 0, "Accordion is not present or not open"

        @allure.title("Check one by one that all chords are present and contain content")
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

    @allure.feature("Autocomplete")
    class TestAutocomplete:
        @allure.title("Check that the field is filled with many random colors")
        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi_with_random_colors()
            colors_result = autocomplete_page.check_color_in_multy()
            assert colors == colors_result, "The Multiple Autocomplete isn't filled, or content was different"

        @allure.title("Check that an item from a filled field can be deleted")
        def test_remove_element_from_multi_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            autocomplete_page.fill_input_multi_with_random_colors()
            value_before, value_after = autocomplete_page.remove_one_value_form_multy()
            assert value_before != value_after, "The element from Multiple Autocomplete isn't deleted"

        @allure.title("Check that the field is filled with single random color")
        def test_single_autocomplete(self, driver):
            autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single_with_random_color()
            output = autocomplete_page.check_color_in_single()
            assert color == output, "The Single Autocomplete isn't filled, or content was different"

    @allure.feature("Date Picker")
    class TestDatePicker:
        @allure.title("Check that the user can select a date in the 'Select Date' field")
        def test_select_date(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            old, new = date_picker_page.set_date()
            assert old != new, "The date picker is not editable"

        @allure.title("Check that the user can select the date and time in the 'Date and Time' field")
        def test_select_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            old, new = date_picker_page.set_date_and_time()
            assert old != new, "The date picker is not editable"

    @allure.feature("Slider")
    class TestSlider:
        @allure.title("Verify that the user can change the slider value")
        def test_slider(self, driver):
            slider_page = SliderPage(driver, "https://demoqa.com/slider")
            slider_page.open()
            before, after = slider_page.change_slider_value()
            assert before != after, "The value of the slider has not been changed"

    @allure.feature("Progress Bar")
    class TestProgressBarPage:
        @allure.feature("Verify that the user can start and stop the 'Progress Bar'")
        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar.open()
            before, after = progress_bar.change_progress_bar_value()
            assert before != after, "The value of the progress bar has not been changed"

    @allure.feature("Tabs")
    class TestTabs:
        @allure.title("Check all tabs one by one")
        def test_all_tabs(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            what_tab, what_tab_content = tabs_page.check_tabs(1)
            origin_tab, origin_tab_content = tabs_page.check_tabs(2)
            use_tab, use_tab_content = tabs_page.check_tabs(3)
            try:
                more_tab, more_tab_content = tabs_page.check_tabs(4)
                assert more_tab == "More" and more_tab_content != 0, "The tab isn't present or not active"
            except TimeoutException:
                assert False, "The tab is not active"
            assert what_tab == "What" and what_tab_content != 0, "The tab isn't present or not active"
            assert origin_tab == "Origin" and origin_tab_content != 0, "The tab isn't present or not active"
            assert use_tab == "Use" and use_tab_content != 0, "The tab isn't present or not active"
            assert more_tab == "More" and more_tab_content != 0, "The tab isn't present or not active"

        @allure.title("Open the 'What' tab and check if content is available")
        def test_what_tab(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            what_tab, what_tab_content = tabs_page.check_tabs(1)
            assert what_tab == "What" and len(what_tab_content) > 0, "The tab isn't present or not active"

        @allure.title("Open the 'Origin' tab and check if content is available")
        def test_origin_tab(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            origin_tab, origin_tab_content = tabs_page.check_tabs(2)
            assert origin_tab == "Origin" and len(origin_tab_content) > 0, "The tab isn't present or not active"

        @allure.title("Open the 'Use' tab and check if content is available")
        def test_use_tab(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            use_tab, use_tab_content = tabs_page.check_tabs(3)
            assert use_tab == "Use" and len(use_tab_content) > 0, "The tab isn't present or not active"

        @allure.title("Open the 'More' tab and check if content is available")
        def test_more_tab(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            try:
                more_tab, more_tab_content = tabs_page.check_tabs(4)
                assert more_tab == "More" and len(more_tab_content) > 0, "The tab isn't present or not active"
            except TimeoutException:
                assert False, "The tab is not active"

    @allure.feature("Tool Tips")
    class TestToolTips:
        @allure.title("Check that the tooltip appears when hovering over the 'Hover me to see' button")
        def test_button_tooltip(self, driver):
            tooltips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tooltips_page.open()
            output = tooltips_page.check_tool_tips(1)
            assert output == 'You hovered over the Button', 'Hover tool-tip is missing or incorrect content'

        @allure.title("Check that the tooltip appears when hovering over the 'Hover me to see' field")
        def test_input_field_tooltip(self, driver):
            tooltips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tooltips_page.open()
            output = tooltips_page.check_tool_tips(2)
            assert output == 'You hovered over the text field', 'Hover tool-tip is missing or incorrect content'

        @allure.title("Check that the tooltip appears when hovering over the 'Contrary' link")
        def test_link_contrary_tooltip(self, driver):
            tooltips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tooltips_page.open()
            output = tooltips_page.check_tool_tips(3)
            assert output == 'You hovered over the Contrary', 'Hover tool-tip is missing or incorrect content'

        @allure.title("Check that the tooltip appears when hovering over the '1.10.32' link")
        def test_link_section_tooltip(self, driver):
            tooltips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tooltips_page.open()
            output = tooltips_page.check_tool_tips(4)
            assert output == 'You hovered over the 1.10.32', 'Hover tool-tip is missing or incorrect content'

    @allure.feature("Menu")
    class TestMenu:
        @allure.title("Check that all 8 menu items and sub-items are present")
        def test_menu_items(self, driver):
            menu_page = MenuPage(driver, "https://demoqa.com/menu")
            menu_page.open()
            output = menu_page.check_menu()
            assert len(output) == 8, 'Menu items are missed'
