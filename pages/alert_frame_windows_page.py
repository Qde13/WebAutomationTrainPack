import random
import time

from locators.alert_frame_windows_locators import BrowserWindowsPageLocators, AlertPageLocators, FramePageLocators, \
    NestedFramePageLocators, ModelDialogPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import UnexpectedAlertPresentException


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
        except UnexpectedAlertPresentException:
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


class FramePage(BasePage):
    locators = FramePageLocators()

    def check_frames_by_index(self, index=int):
        if index == 1:
            frame = self.element_is_visible(self.locators.FIRST_FRAME)
            w, h = frame.get_attribute('width'), frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAMES_HEADING).text
            return [text, w, h]
        elif index == 2:
            frame = self.element_is_visible(self.locators.SECOND_FRAME)
            w, h = frame.get_attribute('width'), frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.FRAMES_HEADING).text
            return [text, w, h]
        else:
            return "Choose 1 or 2"


class NestedFramePage(BasePage):
    locators = NestedFramePageLocators()

    def check_nested_frame(self):
        frames = [self.locators.PARENT_FRAME, self.locators.CHILD_FRAME]
        texts = [self.locators.PARENT_TEXT, self.locators.CHILD_TEXT]
        output = []
        i = 0
        for f in frames:
            self.driver.switch_to.frame(self.element_is_present(f))
            text = self.element_is_present(texts[i]).text
            output.append(text)
            i = i + 1
        return output


class ModelDialogPage(BasePage):
    locators = ModelDialogPageLocators()

    def open_small_dialog(self):
        self.element_is_present(self.locators.SMALL_MODEL_BUTTON).click()

    def open_large_dialog(self):
        self.element_is_present(self.locators.LARGE_MODEL_BUTTON).click()

    def close_small_dialog(self):
        self.element_is_visible(self.locators.CLOSE_SMALL_MODEL).click()

    def close_large_dialog(self):
        self.element_is_visible(self.locators.CLOSE_LARGE_MODEL).click()

    def get_model_header_body_text(self):
        header_text, body_text = (self.element_is_visible(self.locators.MODEL_HEADER).text,
                                  self.element_is_visible(self.locators.MODEL_BODY).text)
        return header_text, body_text
