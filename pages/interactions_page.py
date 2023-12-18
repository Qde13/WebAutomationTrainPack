import random
import time

from selenium.common import TimeoutException

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_item(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_item(self.locators.LIST_ITEM)
        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_sortable_item(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_item(self.locators.GRID_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def get_selectable_item(self, elements):
        try:
            item_list = self.elements_are_visible(elements, timeout=0.5)
            return [item.text for item in item_list]
        except TimeoutException:
            return [""]

    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_items(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        selected_before = self.get_selectable_item(self.locators.LIST_ITEM_ACTIVE)
        self.click_selectable_item(self.locators.LIST_ITEM)
        selected_after = self.get_selectable_item(self.locators.LIST_ITEM_ACTIVE)
        return selected_before, selected_after

    def select_grid_items(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        selected_before = self.get_selectable_item(self.locators.GRID_ITEM_ACTIVE)
        self.click_selectable_item(self.locators.GRID_ITEM)
        selected_after = self.get_selectable_item(self.locators.GRID_ITEM_ACTIVE)
        return selected_before, selected_after


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_visible(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), -500, -300)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def check_that_tab_is_selected(self, tab_element):
        tab = self.element_is_visible(tab_element)
        if tab.get_attribute('aria-selected') != 'true':
            tab.click()

    def check_simple_draggable(self):
        self.check_that_tab_is_selected(self.locators.SIMPLE_TAB)
        drag = self.element_is_visible(self.locators.SIMPLE_DRAG)
        drop = self.element_is_visible(self.locators.SIMPLE_DROP_HERE)
        before = drop.text
        self.action_drag_and_drop_to_element(drag, drop)
        after = drop.text
        return before, after

    def check_accept_draggable(self):
        self.check_that_tab_is_selected(self.locators.ACCEPT_TAB)
        acceptable_drag = self.element_is_visible(self.locators.ACCEPTABLE_DRAG)
        not_acceptable_drag = self.element_is_visible(self.locators.NOT_ACCEPTABLE_DRAG)
        drop = self.element_is_visible(self.locators.ACCEPTABLE_DROP_HERE)
        self.action_drag_and_drop_to_element(not_acceptable_drag, drop)
        after_false_drop = drop.text
        self.action_drag_and_drop_to_element(acceptable_drag, drop)
        after_true_drop = drop.text
        return after_false_drop, after_true_drop

    def check_prevent_propogation_draggable(self):
        self.check_that_tab_is_selected(self.locators.PREVENT_PROPOGATION_TAB)
        drag = self.element_is_visible(self.locators.PREVENT_PROPOGATION_DRAG)
        outer_drop_not_greedy = self.element_is_visible(
            self.locators.PREVENT_PROPOGATION_OUTER_DROP_NOT_GREEDY)
        inner_drop_not_greedy = self.element_is_visible(self.locators.PREVENT_PROPOGATION_INNER_DROP_NOT_GREEDY)
        self.action_drag_and_drop_to_element(drag, inner_drop_not_greedy)
        outer_drop_greedy = self.element_is_visible(self.locators.PREVENT_PROPOGATION_OUTER_DROP_GREEDY)
        inner_drop_greedy = self.element_is_visible(self.locators.PREVENT_PROPOGATION_INNER_DROP_GREEDY)
        self.action_drag_and_drop_to_element(drag, inner_drop_greedy)
        return outer_drop_not_greedy.text.split('\n')[0], outer_drop_greedy.text.split('\n')[0]

    def check_revert_draggable(self, draggable_type):
        draggable = {
            'will':
                {'revert': self.locators.WILL_REVERT_DRAG, },
            'not_will':
                {'revert': self.locators.NOT_REVERT_DRAG, },
        }
        self.check_that_tab_is_selected(self.locators.REVERT_DRAGGABLE_TAB)
        revert = self.element_is_visible(draggable[draggable_type]['revert'])
        drop = self.element_is_visible(self.locators.REVERT_DRAGGABLE_DROP_HERE)
        self.action_drag_and_drop_to_element(revert, drop)
        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_move, position_after_revert

