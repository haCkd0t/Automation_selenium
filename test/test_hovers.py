from pages.hovers import hov

def test_hover(driver,wait):
    ob = hov(driver,wait)
    ob.hvr()