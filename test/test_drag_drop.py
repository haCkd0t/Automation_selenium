from pages.drag_drop_page import Drag_drop


def test_visibilty(driver):
    ob = Drag_drop(driver)
    ob.element_visible()


def test_dragDrop(driver):
    ob = Drag_drop(driver)
    ob.drag_drop()
