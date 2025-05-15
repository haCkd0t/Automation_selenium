import time

from pages.login import Login

def test_login(driver):
    ob = Login(driver)
    ob.Login_valid()
    time.sleep(1)
    ob.Logout()
    time.sleep(2)
    ob.login_invalid_password()
    time.sleep(2)
    ob.login_invalid_username()