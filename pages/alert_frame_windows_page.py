from selenium.webdriver.common.alert import Alert

from locators.alert_frame_windows_locators import BrowserWindowsPageLocators, AlertPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()

    def check_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.switch_to_new_tab()
        heading = self.element_is_visible(self.locators.NEW_TAB_WINDOW_HEADING)
        return str(heading.text)

    def check_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.switch_to_new_tab()
        heading = self.element_is_visible(self.locators.NEW_TAB_WINDOW_HEADING)
        return str(heading.text)


class AlertPage(BasePage):

    locators = AlertPageLocators()

    def check_alert_appear(self):
        self.element_is_visible(self.locators.AlERT_APPEAR_BUTTON).click()
        # alert_window
