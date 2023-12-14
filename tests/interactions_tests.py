from pages.interactions_page import SortablePage


class TestInteractions:
    class TestSortable:
        def test_sortable_list(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            before, after = sortable_page.change_list_order()
            assert before != after, "the order of the list has not been changed"

        def test_sortable_grid(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            before, after = sortable_page.change_grid_order()
            assert before != after, "the order of the grid has not been changed"

        def test_sortable_one_by_one(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            before_list, after_list = sortable_page.change_list_order()
            before_grid, after_grid = sortable_page.change_grid_order()
            assert before_list != after_list, "the order of the list has not been changed"
            assert before_grid != after_grid, "the order of the grid has not been changed"


