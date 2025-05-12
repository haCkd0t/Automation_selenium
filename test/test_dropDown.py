from pages.drop_down import drop_Down


def test_drop(driver):
    drop_Down_o = drop_Down(driver)
    drop_Down_o.Select_option_1()
    drop_Down_o.Select_option_2()