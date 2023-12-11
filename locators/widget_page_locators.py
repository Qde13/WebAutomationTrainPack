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


class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, "#datePickerMonthYearInput")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, "select.react-datepicker__month-select")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, "select.react-datepicker__year-select")

    # Day list selector works for both date and date&time pickers
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

    DATE_TIME_INPUT = (By.CSS_SELECTOR, "#dateAndTimePickerInput")
    DATE_TIME_SELECT_MONTH = (By.CSS_SELECTOR, "div.react-datepicker__month-read-view")
    DATE_TIME_SELECT_YEAR = (By.CSS_SELECTOR, "div.react-datepicker__year-read-view")
    DATE_TIME_SELECT_MONTH_LIST = (By.CSS_SELECTOR, "div.react-datepicker__month-option")
    DATE_TIME_SELECT_YEAR_LIST = (By.CSS_SELECTOR, "div.react-datepicker__year-option")
    DATE_TIME_SELECT_TIME_LIST = (By.CSS_SELECTOR, "li.react-datepicker__time-list-item ")


class SliderPageLocators:
    SLIDER_VALUE = (By.CSS_SELECTOR, "#sliderValue")
    INPUT_SLIDER = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")


class ProgressBarPageLocators:
    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, "#startStopButton")
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")

