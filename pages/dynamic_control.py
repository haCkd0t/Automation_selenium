import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class dyan_con:
    def __init__(self,driver,wait):
        self.wait = wait
        self.driver = driver

    def check_box(self):
        self.driver.get("https://the-internet.herokuapp.com/dynamic_controls")
        time.sleep(2)
        checkbox = self.driver.find_element(By.XPATH,value="//div[@id='checkbox']")
        is_displayed = checkbox.is_displayed()
        assert is_displayed, "Failed"
        self.driver.find_element(By.XPATH,value="//button[@onclick='swapCheckbox()']").click()
        f = self.wait.until(EC.invisibility_of_element_located(checkbox))
        assert f, "Test Failed"

    def input(self):
        self.driver.get("https://the-internet.herokuapp.com/dynamic_controls")
        time.sleep(2)
        inpt_d = self.driver.find_element(By.XPATH,value="//input[@type='text']")
        assert inpt_d.get_attribute("disabled") is not None,"Test Failed"
        self.driver.find_element(By.XPATH,value="//button[@onclick='swapInput()']").click()
        self.wait.until(lambda driver: inpt_d.is_enabled())
        assert inpt_d.is_enabled(),"Failed"




