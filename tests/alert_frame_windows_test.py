import allure

from pages.alert_frame_windows_page import BrowserWindowsPage, AlertPage, FramePage, NestedFramePage, \
    ModalDialogPage


@allure.suite("Alerts Frame Windows page tests")
class TestAlertsFrameWindows:
    @allure.feature('Browser Windows')
    class TestBrowserWindows:
        @allure.title("Check that the link opens in a new tab")
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            result = browser_windows_page.check_new_tab()
            assert result == "This is a sample page", "The new web tab wasn't open"

        @allure.title("Check that the link opens in a new window")
        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            result = browser_windows_page.check_new_window()
            assert result == "This is a sample page", "The new window wasn't open"

    @allure.feature('Alerts')
    class TestAlerts:
        @allure.title("Check that the alert appear")
        def test_alert_appear(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_alert_appear()
            assert alert_text == "You clicked a button", "The alert didn't appear"

        @allure.title("Check that the alert appear after 5 sec")
        def test_alert_appear_after_five_sec(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_alert_appear_five_sec()
            assert alert_text == "This alert appeared after 5 seconds", "The alert didn't appear after five seconds"

        @allure.title("Check that the confirmation alert appear")
        def test_confirm_confirmation_alert(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_result = alert_page.check_accept_confirm_alert()
            assert alert_result == "You selected Ok", "The alert didn't appear or result was different"

        @allure.title("Check that the confirmation alert can be canceled")
        def test_cancel_confirmation_alert(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_result = alert_page.check_cancel_confirm_alert()
            assert alert_result == "You selected Cancel", "The alert didn't appear or result was different"

        @allure.title("Check that the prompt alert functional")
        def test_prompt_alert(self, driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            text, prompt_result = alert_page.check_prompt_alert()
            assert prompt_result == f"You entered {text}", "The alert didn't appear or result was different"

    @allure.feature("Frames")
    class TestFrames:
        @allure.title("Check that the 500px by 350px frame is present")
        def test_first_frame(self, driver):
            frame_page = FramePage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result = frame_page.check_frames_by_index(1)
            assert result == ["This is a sample page", "500px", "350px"], ("The Frame doesn't exist,"
                                                                           " or result was different")

        @allure.title("Check that the 100px by 100px frame is present")
        def test_second_frame(self, driver):
            frame_page = FramePage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result = frame_page.check_frames_by_index(2)
            assert result == ["This is a sample page", "100px", "100px"], ("The Frame doesn't exist,"
                                                                           " or result was different")

    @allure.feature("Nested Frames")
    class TestNestedFrames:
        @allure.title("Check that the nested frames are present")
        def test_nested_frame(self, driver):
            nested_frame = NestedFramePage(driver, "https://demoqa.com/nestedframes")
            nested_frame.open()
            output = nested_frame.check_nested_frame()
            assert output == ["Parent frame", "Child Iframe"], "The Frame doesn't exist, or result was different"

    @allure.feature("Modal Dialog")
    class TestModalDialog:
        @allure.title("Check that the small modal dialog is opened")
        def test_small_model_dialog(self, driver):
            modal_dialog = ModalDialogPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialog.open()
            modal_dialog.open_small_dialog()
            header, body = modal_dialog.get_model_header_body_text()
            modal_dialog.close_small_dialog()
            assert header == "Small Modal", "Modal isn't open, or header is different"
            assert len(body) <= 55, "Body is longer then 55 chars"

        @allure.title("Check that the large modal dialog is opened")
        def test_large_model_dialog(self, driver):
            model_dialog = ModalDialogPage(driver, "https://demoqa.com/modal-dialogs")
            model_dialog.open()
            model_dialog.open_large_dialog()
            header, body = model_dialog.get_model_header_body_text()
            model_dialog.close_large_dialog()
            assert header == "Large Modal", "Modal isn't open, or header is different"
            assert len(body) >= 55, "Body is shorter then 55 chars"
