from pages.widget_page import AccordianPage, AutocompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage


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

    class TestTabs:

        def test_all_tabs(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            what_tab, what_tab_content = tabs_page.check_tabs(1)
            origin_tab, origin_tab_content = tabs_page.check_tabs(2)
            use_tab, use_tab_content = tabs_page.check_tabs(3)
            more_tab, more_tab_content = tabs_page.check_tabs(4)
            assert what_tab == "What" and what_tab_content != 0, "The tab isn't present or not active"
            assert origin_tab == "Origin" and origin_tab_content != 0, "The tab isn't present or not active"
            assert use_tab == "Use" and use_tab_content != 0, "The tab isn't present or not active"
            assert more_tab == "More" and more_tab_content != 0, "The tab isn't present or not active"

        def test_what_tab(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            what_tab, what_tab_content = tabs_page.check_tabs(1)
            assert what_tab == "What" and len(what_tab_content) > 0, "The tab isn't present or not active"

        def test_origin_tab(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            origin_tab, origin_tab_content = tabs_page.check_tabs(2)
            assert origin_tab == "Origin" and len(origin_tab_content) > 0, "The tab isn't present or not active"

        def test_use_tab(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            use_tab, use_tab_content = tabs_page.check_tabs(3)
            assert use_tab == "Use" and len(use_tab_content) > 0, "The tab isn't present or not active"

        def test_more_tab(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            more_tab, more_tab_content = tabs_page.check_tabs(4)
            assert more_tab == "More" and len(more_tab_content) > 0, "The tab isn't present or not active"

    class TestToolTips:
        def test_button_tooltip(self, driver):
            tooltips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tooltips_page.open()
            output = tooltips_page.check_tool_tips(1)
            assert output == 'You hovered over the Button', 'Hover tool-tip is missing or incorrect content'

        def test_input_field_tooltip(self, driver):
            tooltips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tooltips_page.open()
            output = tooltips_page.check_tool_tips(2)
            assert output == 'You hovered over the text field', 'Hover tool-tip is missing or incorrect content'

        def test_link_contrary_tooltip(self, driver):
            tooltips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tooltips_page.open()
            output = tooltips_page.check_tool_tips(3)
            assert output == 'You hovered over the Contrary', 'Hover tool-tip is missing or incorrect content'

        def test_link_section_tooltip(self, driver):
            tooltips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tooltips_page.open()
            output = tooltips_page.check_tool_tips(4)
            assert output == 'You hovered over the 1.10.32', 'Hover tool-tip is missing or incorrect content'

    class TestMenu:
        def test_menu_items(self, driver):
            menu_page = MenuPage(driver, "https://demoqa.com/menu")
            menu_page.open()
            output = menu_page.check_menu()
            assert len(output) == 8, 'Menu items are missed'

    # Need fix
    class TestSelectMenu:
        def test_select_value(self, driver):
            select_menu = SelectMenuPage(driver, "https://demoqa.com/select-menu")
            select_menu.open()
            output = select_menu.check_select_value()
            print(output)
            assert False
