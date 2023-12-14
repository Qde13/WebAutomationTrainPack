from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "#demo-tab-list")
    LIST_ITEM = (By.CSS_SELECTOR, "div#demo-tabpane-list div[class='list-group-item list-group-item-action']")
    TAB_GRID = (By.CSS_SELECTOR, "#demo-tab-grid")
    GRID_ITEM = (By.CSS_SELECTOR, "div#demo-tabpane-grid div[class='list-group-item list-group-item-action']")
