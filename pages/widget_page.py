import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.genereator import generated_color
from locators.widget_page_locators import AccordianPageLocators, AutocompletePageLocators
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
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2,5))
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

