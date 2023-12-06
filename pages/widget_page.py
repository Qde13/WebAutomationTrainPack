from selenium.common import TimeoutException

from locators.widget_page_locators import AccordianPageLocators
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

