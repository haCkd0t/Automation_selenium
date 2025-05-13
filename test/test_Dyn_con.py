from pages.dynamic_content import dyn_con

def test_dyn(driver):
    ob = dyn_con(driver)
    ob.check_dyn_cont()
