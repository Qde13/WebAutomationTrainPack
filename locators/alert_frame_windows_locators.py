from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:

    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "#tabButton")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "#windowButton")

    NEW_TAB_WINDOW_HEADING = (By.CSS_SELECTOR, "#sampleHeading")


class AlertPageLocators:

    # Alert buttons
    AlERT_APPEAR_BUTTON = (By.CSS_SELECTOR, "#alertButton")
    ALERT_APPEAR_AFTER_FIVE_SEC_BUTTON = (By.CSS_SELECTOR, "#timerAlertButton")
    CONFIRM_BOX_BUTTON = (By.CSS_SELECTOR, "#confirmButton")
    PROMPT_BOX_BUTTON = (By.CSS_SELECTOR, "#promtButton")

    # Results text fields
    CONFIRM_BOX_RESULT = (By.CSS_SELECTOR, "#confirmResult")
    PROMPT_BOX_RESULT = (By.CSS_SELECTOR, "#promptResult")


class FramePageLocators:

    FIRST_FRAME = (By.CSS_SELECTOR, "iframe#frame1")
    SECOND_FRAME = (By.CSS_SELECTOR, "iframe#frame2")

    FRAMES_HEADING = (By.CSS_SELECTOR, "#sampleHeading")
