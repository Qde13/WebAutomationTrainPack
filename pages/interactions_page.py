import random

from selenium.common import TimeoutException

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
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

