from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "#demo-tab-list")
    LIST_ITEM = (By.CSS_SELECTOR, "div#demo-tabpane-list div[class='list-group-item list-group-item-action']")
    TAB_GRID = (By.CSS_SELECTOR, "#demo-tab-grid")
    GRID_ITEM = (By.CSS_SELECTOR, "div#demo-tabpane-grid div[class='list-group-item list-group-item-action']")


class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "#demo-tab-list")
    LIST_ITEM = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item list-group-item-action']")
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item active list-group-item-action']")
    TAB_GRID = (By.CSS_SELECTOR, "#demo-tab-grid")
    GRID_ITEM = (By.CSS_SELECTOR, "li[class='list-group-item list-group-item-action']")
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, "li[class='list-group-item active list-group-item-action']")


class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, "div#resizableBoxWithRestriction"
                                             " span[class='react-resizable-handle react-resizable-handle-se']")
    RESIZABLE_BOX = (By.CSS_SELECTOR, "div#resizableBoxWithRestriction")
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, "div#resizable span[class='react-resizable-handle react-resizable-handle-se']")
    RESIZABLE = (By.CSS_SELECTOR, "div#resizable")


class DroppablePageLocators:
    SIMPLE_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-simple")
    SIMPLE_DRAG = (By.CSS_SELECTOR, "#draggable")
    SIMPLE_DROP_HERE = (By.CSS_SELECTOR, "#simpleDropContainer #droppable")

    ACCEPT_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-accept")
    ACCEPTABLE_DRAG = (By.CSS_SELECTOR, "#acceptable")
    NOT_ACCEPTABLE_DRAG = (By.CSS_SELECTOR, "#notAcceptable")
    ACCEPTABLE_DROP_HERE = (By.CSS_SELECTOR, "#acceptDropContainer #droppable")

    PREVENT_PROPOGATION_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-preventPropogation")
    PREVENT_PROPOGATION_DRAG = (By.CSS_SELECTOR, "#dragBox")
    PREVENT_PROPOGATION_OUTER_DROP_NOT_GREEDY = (By.CSS_SELECTOR, "#notGreedyDropBox")
    PREVENT_PROPOGATION_INNER_DROP_NOT_GREEDY = (By.CSS_SELECTOR, "#notGreedyInnerDropBox")
    PREVENT_PROPOGATION_OUTER_DROP_GREEDY = (By.CSS_SELECTOR, "#greedyDropBox")
    PREVENT_PROPOGATION_INNER_DROP_GREEDY = (By.CSS_SELECTOR, "#greedyDropBoxInner")

    REVERT_DRAGGABLE_TAB = (By.CSS_SELECTOR, "#droppableExample-tab-revertable")
    WILL_REVERT_DRAG = (By.CSS_SELECTOR, "#revertable")
    NOT_REVERT_DRAG = (By.CSS_SELECTOR, "#notRevertable")
    REVERT_DRAGGABLE_DROP_HERE = (By.CSS_SELECTOR, "#revertableDropContainer #droppable")


class DraggablePageLocators:
    SIMPLE_TAB = (By.CSS_SELECTOR, "#draggableExample-tab-simple")
    SIMPLE_DRAG_ME = (By.CSS_SELECTOR, "#dragBox")

    AXIS_RESTRICTED_TAB = (By.CSS_SELECTOR, "#draggableExample-tab-axisRestriction")
    AXIS_RESTRICTED_ONLY_X_DRAG = (By.CSS_SELECTOR, "#restrictedX")
    AXIS_RESTRICTED_ONLY_Y_DRAG = (By.CSS_SELECTOR, "#restrictedY")

    CONTAINER_RESTRICTED_TAB = (By.CSS_SELECTOR, "#draggableExample-tab-containerRestriction")
    CONTAINER_RESTRICTED_DRAG_BOX = (By.CSS_SELECTOR,
                                     "div[class='draggable ui-widget-content ui-draggable ui-draggable-handle']")
    CONTAINER_RESTRICTED_DRAG_SPAN = (By.CSS_SELECTOR, "span[class='ui-widget-header ui-draggable ui-draggable-handle']")

    CURSOR_STYLE_TAB = (By.CSS_SELECTOR, "#draggableExample-tab-cursorStyle")
    CURSOR_STYLE_CURSOR_CENTER = (By.CSS_SELECTOR, "#cursorCenter")
    CURSOR_STYLE_CURSOR_TOP_LEFT = (By.CSS_SELECTOR, "#cursorTopLeft")
    CURSOR_STYLE_CURSOR_BOTTOM = (By.CSS_SELECTOR, "#cursorBottom")


