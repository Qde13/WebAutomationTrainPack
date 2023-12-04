import random
import time

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
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_appear_five_sec(self):
        self.element_is_visible(self.locators.ALERT_APPEAR_AFTER_FIVE_SEC_BUTTON).click()
        time.sleep(5)
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentExeption:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    def check_accept_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        result = self.element_is_visible(self.locators.CONFIRM_BOX_RESULT)
        return result.text

    def check_cancel_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.dismiss()
        result = self.element_is_visible(self.locators.CONFIRM_BOX_RESULT)
        return result.text

    def check_prompt_alert(self):
        text = f"autotest {random.randint(0, 999)}"
        self.element_is_visible(self.locators.PROMPT_BOX_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        result = self.element_is_visible(self.locators.PROMPT_BOX_RESULT)
        return text, result.text
