import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.genereator import generated_color, generated_date
from locators.widget_page_locators import AccordianPageLocators, AutocompletePageLocators, DatePickerPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian_by_index(self, accordian_index):
        accordian = {1: {'title': self.locators.SECTION_FIRST,
                         'content': self.locators.SECTION_FIRST_CONTENT},
                     2: {'title': self.locators.SECTION_SECOND,
                         'content': self.locators.SECTION_SECOND_CONTENT},
                     3: {'title': self.locators.SECTION_THIRD,
                         'content': self.locators.SECTION_THIRD_CONTENT}
                     }
        section_title = self.element_is_present(accordian[accordian_index]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_index]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_index]['content']).text
        return section_title.text, section_content


class AutocompletePage(BasePage):
    locators = AutocompletePageLocators()

    def fill_input_multi_with_random_colors(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multy = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multy.send_keys(color)
            input_multy.send_keys(Keys.ENTER)
        return colors

    def remove_one_value_form_multy(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multy(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single_with_random_color(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        single_input = self.element_is_clickable(self.locators.SINGLE_INPUT)
        single_input.send_keys(color)
        single_input.send_keys(Keys.ENTER)
        return color

    def check_color_in_single(self):
        color_value = self.element_is_visible(self.locators.SINGLE_VALUE).text
        return [color_value]


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def set_date(self):
        date = next(generated_date())
        input_date = self.element_is_present(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def set_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_present(self.locators.DATE_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_present(self.locators.DATE_TIME_SELECT_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_TIME_SELECT_MONTH_LIST, date.month)
        self.element_is_present(self.locators.DATE_TIME_SELECT_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_TIME_SELECT_YEAR_LIST, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.element_is_present(self.locators.DATE_TIME_INPUT).click()
        self.set_date_item_from_list(self.locators.DATE_TIME_SELECT_TIME_LIST, date.time)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break
