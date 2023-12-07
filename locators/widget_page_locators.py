from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, "#section1Heading")
    SECTION_FIRST_CONTENT = (By.CSS_SELECTOR, "#section1Content p")

    SECTION_SECOND = (By.CSS_SELECTOR, "#section2Heading")
    SECTION_SECOND_CONTENT = (By.CSS_SELECTOR, "#section2Content p")

    SECTION_THIRD = (By.CSS_SELECTOR, "#section3Heading")
    SECTION_THIRD_CONTENT = (By.CSS_SELECTOR, "#section3Content p")


class AutocompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, "input#autoCompleteMultipleInput")
    MULTI_VALUE = (By.CSS_SELECTOR, "div[class='css-12jo7m5 auto-complete__multi-value__label']")
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, "div[class='css-xb97g8 auto-complete__multi-value__remove']")
    SINGLE_INPUT = (By.CSS_SELECTOR, "input#autoCompleteSingleInput")
    SINGLE_VALUE = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")

