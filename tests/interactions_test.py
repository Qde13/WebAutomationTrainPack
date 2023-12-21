import allure

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.suite("Interactions page tests")
class TestInteractions:
    @allure.feature("Sortable")
    class TestSortable:
        @allure.title("Check that the order of list items can change")
        def test_sortable_list(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            before, after = sortable_page.change_list_order()
            assert before != after, "the order of the list has not been changed"

        @allure.title("Check that the order of grid items can change")
        def test_sortable_grid(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            before, after = sortable_page.change_grid_order()
            assert before != after, "the order of the grid has not been changed"

        @allure.title("Check that the order of list and grid items can change one by one")
        def test_sortable_one_by_one(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            before_list, after_list = sortable_page.change_list_order()
            before_grid, after_grid = sortable_page.change_grid_order()
            assert before_list != after_list, "the order of the list has not been changed"
            assert before_grid != after_grid, "the order of the grid has not been changed"

    @allure.feature("Selectable")
    class TestSelectable:
        @allure.title("Check that the list item can be selected")
        def test_selectable_list(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            before, after = selectable_page.select_list_items()
            assert before != after

        @allure.title("Check that the grid item can be selected")
        def test_selectable_grid(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            before, after = selectable_page.select_grid_items()
            assert before != after

        @allure.title("Check that the list and grid item can be selected one by one")
        def test_selectable_one_by_one(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            before_list, after_list = selectable_page.select_list_items()
            before_grid, after_grid = selectable_page.select_grid_items()
            assert before_list != after_list
            assert before_grid != after_grid

    @allure.feature("Resizeable")
    class TestResizable:
        @allure.title("Check that the restricted resizable box can be modified")
        def test_resizable_box(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            max_size, min_size = resizable_page.change_size_resizable_box()
            assert max_size == ('500px', '300px'), "The Max size of Resizable box isn't 500px, 300px"
            assert min_size == ('150px', '150px'), "The Min size of Resizable box isn't 150px, 150px"

        @allure.title("Check that the resizable box can be modified")
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            max_size, min_size = resizable_page.change_size_resizable()
            assert max_size != min_size, "The resizeable box isn't changed"

    @allure.feature("Droppable")
    class TestDroppable:
        @allure.title("Check that the item can be moved to the 'Drop here' field")
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            before, after = droppable_page.check_simple_draggable()
            assert after == 'Dropped!', "The element has not been dropped"

        @allure.title("Check that the acceptable item can be moved to the 'Drop here' field")
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            after_false, after_true = droppable_page.check_accept_draggable()
            assert after_false == 'Drop here', "The element has been dropped"
            assert after_true == 'Dropped!', "The element has not been dropped"

        @allure.title("Check behavior of outer and inner droppable fields")
        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_greedy, greedy = droppable_page.check_prevent_propogation_draggable()
            assert not_greedy == 'Dropped!', "The element has not been dropped"
            assert greedy != 'Dropped!', "The element has been dropped"

        @allure.title("Check that the 'Will Revert' element returns to its original position")
        def test_will_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            after_move, after_revert = droppable_page.check_revert_draggable('will')
            assert after_move != after_revert, "The element has not been revert"

        @allure.title("Check that the 'Not Revert' element does not return to its original position ")
        def test_not_will_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            after_move, after_revert = droppable_page.check_revert_draggable('not_will')
            assert after_move == after_revert, "The element has been revert"

    @allure.feature("Draggable")
    class TestDraggable:
        @allure.title("Check that the 'Drag Me' element can be moved in any direction")
        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            before, after = draggable_page.check_simple_drag_box()
            assert before != after, "The position of the drag box has not been changed"

        @allure.title("Check that 'Only X' and 'Only Y' elements can only be moved along the corresponding axis")
        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            before_x, after_x, before_y, after_y = draggable_page.check_axis_restricted()
            assert before_x != after_x, "The position of the drag box has not been changed"
            assert before_y != after_y, "The position of the drag box has not been changed"
