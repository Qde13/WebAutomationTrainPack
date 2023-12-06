from pages.widget_page import AccordianPage


class TestWidgets:
    class TestAccordian:

        def test_first_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            title, content = accordian_page.check_accordian_by_index(1)
            assert title == "What is Lorem Ipsum?" and len(content) > 0, "Accordion is not present or not open"

        def test_second_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            title, content = accordian_page.check_accordian_by_index(2)
            assert title == "Where does it come from?" and len(content) > 0, "Accordion is not present or not open"

        def test_third_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            title, content = accordian_page.check_accordian_by_index(3)
            assert title == "Why do we use it?" and len(content) > 0, "Accordion is not present or not open"

        def test_accordian_one_by_one(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian_by_index(1)
            assert first_title == "What is Lorem Ipsum?" and len(first_content) > 0, \
                "Accordion is not present or not open"
            second_title, second_content = accordian_page.check_accordian_by_index(2)
            assert second_title == "Where does it come from?" and len(second_content) > 0, \
                "Accordion is not present or not open"
            third_title, third_content = accordian_page.check_accordian_by_index(3)
            assert third_title == "Why do we use it?" and len(third_content) > 0, \
                "Accordion is not present or not open"
