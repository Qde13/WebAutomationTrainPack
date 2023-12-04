from pages.alert_frame_windows_page import BrowserWindowsPage, AlertPage, FramePage


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

    class TestFrames:
        def test_first_frame(self, driver):
            frame_page = FramePage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result = frame_page.check_frames_by_index(1)
            assert result == ["This is a sample page", "500px", "350px"], ("The Frame doesn't exist,"
                                                                           " or result was different")

        def test_second_frame(self, driver):
            frame_page = FramePage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result = frame_page.check_frames_by_index(2)
            assert result == ["This is a sample page", "100px", "100px"], ("The Frame doesn't exist,"
                                                                           " or result was different")

