from pages.widget_page import AccordianPage


class TestWidgets:

    class TestAccordian:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
