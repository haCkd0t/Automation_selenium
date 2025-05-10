from test import actions
def test_checkbox(driver,wait):
    result = actions.check_box(driver,wait)
    assert result,"Failed"