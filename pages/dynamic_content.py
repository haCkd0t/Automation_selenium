import time

from selenium.webdriver.common.by import By


class dyn_con:
    def __init__(self,driver):
        self.driver = driver

    def check_dyn_cont(self):
        self.driver.get("https://the-internet.herokuapp.com/dynamic_content?with_content=static")
        ele1_text_b = self.driver.find_element(By.XPATH, "(//*[@class='large-10 columns'])[1]").text
        ele2_text_b = self.driver.find_element(By.XPATH, "(//*[@class='large-10 columns'])[2]").text
        ele3_text_b = self.driver.find_element(By.XPATH, "(//*[@class='large-10 columns'])[3]").text
        time.sleep(4)
        self.driver.refresh()
        time.sleep(4)
        ele1_text_a = self.driver.find_element(By.XPATH, "(//*[@class='large-10 columns'])[1]").text
        ele2_text_a = self.driver.find_element(By.XPATH, "(//*[@class='large-10 columns'])[2]").text
        ele3_text_a = self.driver.find_element(By.XPATH, "(//*[@class='large-10 columns'])[3]").text
        assert ele1_text_a == ele1_text_b , "Failed"
        assert ele2_text_a == ele2_text_b , "Failed"
        assert ele3_text_a != ele3_text_b, "Failed"


