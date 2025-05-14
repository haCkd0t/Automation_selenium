from pages.dynamic_control import dyan_con

def test_checkbox(driver,wait):
    ob = dyan_con(driver,wait)
    r = ob.check_box()

def test_input(driver,wait):
    ob = dyan_con(driver,wait)
    r = ob.input()