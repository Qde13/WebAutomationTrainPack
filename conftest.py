import datetime

import allure
import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    try:
        attach = driver.get_screenshot_as_png()
        allure.attach(attach, name=f"Screenshot {datetime.datetime.today()}",
                      attachment_type=allure.attachment_type.PNG)
        driver.quit()
    except:
        driver.quit()
