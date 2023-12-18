from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


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

    class TestSelectable:
        def test_selectable_list(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            before, after = selectable_page.select_list_items()
            assert before != after

        def test_selectable_grid(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            before, after = selectable_page.select_grid_items()
            assert before != after

        def test_selectable_one_by_one(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            before_list, after_list = selectable_page.select_list_items()
            before_grid, after_grid = selectable_page.select_grid_items()
            assert before_list != after_list
            assert before_grid != after_grid

    class TestResizable:
        def test_resizable_box(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            max_size, min_size = resizable_page.change_size_resizable_box()
            assert max_size == ('500px', '300px'), "The Max size of Resizable box isn't 500px, 300px"
            assert min_size == ('150px', '150px'), "The Min size of Resizable box isn't 150px, 150px"

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            max_size, min_size = resizable_page.change_size_resizable()
            assert max_size != min_size, "The resizeable box isn't changed"

    class TestDroppable:
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            before, after = droppable_page.check_simple_draggable()
            assert after == 'Dropped!', "The element has not been dropped"

        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            after_false, after_true = droppable_page.check_accept_draggable()
            assert after_false == 'Drop here', "The element has been dropped"
            assert after_true == 'Dropped!', "The element has not been dropped"

        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_greedy, greedy = droppable_page.check_prevent_propogation_draggable()
            assert not_greedy == 'Dropped!', "The element has not been dropped"
            assert greedy != 'Dropped!', "The element has been dropped"

        def test_will_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            after_move, after_revert = droppable_page.check_revert_draggable('will')
            assert after_move != after_revert, "The element has not been revert"

        def test_not_will_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            after_move, after_revert = droppable_page.check_revert_draggable('not_will')
            assert after_move == after_revert, "The element has been revert"

