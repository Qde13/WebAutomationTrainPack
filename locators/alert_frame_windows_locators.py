from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:

    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "#tabButton")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "#windowButton")

    NEW_TAB_WINDOW_HEADING = (By.CSS_SELECTOR, "#sampleHeading")


class AlertPageLocators:

    AlERT_APPEAR_BUTTON = (By.CSS_SELECTOR, "#alertButton")
    ALERT_APPEAR_AFTER_FIVE_SEC_BUTTON = (By.CSS_SELECTOR, "#timerAlertButton")
    CONFIRM_BOX_BUTTON = (By.CSS_SELECTOR, "#confirmButton")
    PROMPT_BOX_BUTTON = (By.CSS_SELECTOR, "#promtButton")

