import time

from pages.Add_remove_element_page import AddRemoveElement


def test_Add_element_click(driver):
    login_object = AddRemoveElement(driver)
    login_object.open_url("https://the-internet.herokuapp.com/add_remove_elements/")
    time.sleep(1)
    login_object.verify_Add_button_and_click()


def test_remove_element_click(driver):
    login_object = AddRemoveElement(driver)
    login_object.open_url("https://the-internet.herokuapp.com/add_remove_elements/")
    time.sleep(1)
    login_object.verify_Add_button_and_click()
    time.sleep(1)
    login_object.verify_remove_button_click()
