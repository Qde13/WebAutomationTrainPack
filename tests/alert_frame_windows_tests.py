from pages.alert_frame_windows_page import BrowserWindowsPage, AlertPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            result = browser_windows_page.check_new_tab()
            assert result == "This is a sample page", "The new web tab wasn't open"

        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            result = browser_windows_page.check_new_window()
            assert result == "This is a sample page", "The new window wasn't open"

    class TestAlerts:
        def test_alert_appear(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_alert_appear()
            assert alert_text == "You clicked a button", "The alert didn't appear"

        def test_alert_appear_after_five_sec(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_alert_appear_five_sec()
            assert alert_text == "This alert appeared after 5 seconds", "The alert didn't appear after five seconds"

        def test_confirm_confirmation_alert(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_result = alert_page.check_accept_confirm_alert()
            assert alert_result == "You selected Ok", "The alert didn't appear or result was different"

        def test_cancel_confirmation_alert(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_result = alert_page.check_cancel_confirm_alert()
            assert alert_result == "You selected Cancel", "The alert didn't appear or result was different"

        def test_prompt_alert(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            text, prompt_result = alert_page.check_prompt_alert()
            assert prompt_result == f"You entered {text}", "The alert didn't appear or result was different"
