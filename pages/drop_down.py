import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class drop_Down:
    def __init__(self,driver):
        self.driver = driver

    def Select_option_1(self):
        self.driver.get("https://the-internet.herokuapp.com/dropdown")
        dropDown = self.driver.find_element(By.XPATH,value="//select")
        select = Select(dropDown)
        select.select_by_visible_text("Option 1")
        time.sleep(4)
        assert "1" in dropDown.text, "Fail"
    def Select_option_2(self):
        self.driver.get("https://the-internet.herokuapp.com/dropdown")
        dropDown = self.driver.find_element(By.XPATH,value="//select")
        select = Select(dropDown)
        select.select_by_visible_text("Option 2")
        time.sleep(4)
        assert "2" in dropDown.text, "Fail"