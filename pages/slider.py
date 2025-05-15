import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class slide:
    def __init__(self,driver):
        self.driver = driver

    def sld(self):
        self.driver.get("https://the-internet.herokuapp.com/horizontal_slider")
        action = ActionChains(self.driver)
        r = self.driver.find_element(By.XPATH,value="//span").text
        slider = self.driver.find_element(By.XPATH,value="//input")
        action.click_and_hold(slider).move_by_offset(50,0).release().perform()
        time.sleep(5)
        rr  = self.driver.find_element(By.XPATH,value="//span").text
        r = int(r)
        rr = float(rr)
        assert r < rr , "Test Failed"
