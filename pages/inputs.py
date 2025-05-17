import time

from selenium.webdriver.common.by import By

class inp:
    def __init__(self,driver,inptt):
        self.driver = driver
        self.inptt = inptt
    def inpt(self):
        self.driver.get("https://the-internet.herokuapp.com/inputs")
        self.driver.find_element(By.XPATH, "//input").send_keys(str(self.inptt))
        time.sleep(2)
