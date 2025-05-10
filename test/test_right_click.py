from test import actions
def test_rightClick(driver,wait):
    r = actions.right_click_alert(driver,wait)
    assert "You selected a context menu" in r, "Test Failed"