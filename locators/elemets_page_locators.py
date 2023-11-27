from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "#userName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:

    YES_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    NO_BUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class WebTablePageLocators:

    # Add and Edit person form
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    EDIT_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    AGE = (By.CSS_SELECTOR, "#age")
    SALARY = (By.CSS_SELECTOR, "#salary")
    DEPARTMENT = (By.CSS_SELECTOR, "#department")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")

    # Tables
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, ".rt-tr-group")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#searchBox")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    EMPTY_TABLE = (By.CSS_SELECTOR, "div.rt-noData")
    ROW_COUNT = (By.CSS_SELECTOR, "select[aria-label='rows per page']")


class ButtonsPageLocators:
    # buttons
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "#doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "#rightClickBtn")
    CLICK_BUTTON = (By.XPATH, '//button[text()="Click Me"]')

    # messages
    DOUBLE_CLICK_BUTTON_MESSAGE = (By.CSS_SELECTOR, "#doubleClickMessage")
    RIGHT_CLICK_BUTTON_MESSAGE = (By.CSS_SELECTOR, "#rightClickMessage")
    CLICK_BUTTON_MESSAGE = (By.CSS_SELECTOR, "#dynamicClickMessage")


class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, "#simpleLink")
    BAD_REQUEST = (By.CSS_SELECTOR, "#bad-request")


class UploadAndDownloadPageLocators:
    UPLOAD_FILE_INPUT = (By.CSS_SELECTOR, "input#uploadFile")
    UPLOADED_FILEPATH = (By.CSS_SELECTOR, "#uploadedFilePath")
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "#downloadButton")


