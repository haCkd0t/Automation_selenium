import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class dyn_loading:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait


    def gif(self):
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        self.driver.find_element(By.XPATH,value="//button").click()
        gif = (By.XPATH,"(//img)[2]")
        a = self.wait.until(EC.visibility_of_element_located(gif))
        assert a,"Test Failed"
        time.sleep(7)
        b = a = self.wait.until(EC.invisibility_of_element(gif))
        assert b, "Test Failed"

    def hello_world(self):
        helw = (By.XPATH,"/html/body/div[2]/div/div/div[3]/h4")
        r = a = self.wait.until(EC.visibility_of_element_located(helw))
        assert r , "Test Failed"

    def presence_of_element(self):
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        self.driver.find_element(By.XPATH,value="//button").click()
        time.sleep(7)
        a = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/h4")))
        assert a, "Test Failed"



