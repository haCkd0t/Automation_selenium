import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class hov:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def hvr(self):
        self.driver.get("https://the-internet.herokuapp.com/hovers")
        action = ActionChains(self.driver)
        user1 = self.driver.find_element(By.XPATH,value="(//img)[2]")
        action.move_to_element(user1).perform()
        r1 = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//h5[text()='name: user1']")))
        assert r1 , "Test Failed"
        user2 = self.driver.find_element(By.XPATH, value="(//img)[3]")
        action.move_to_element(user2).perform()
        r2 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h5[text()='name: user2']")))
        assert r2, "Test Failed"
        user3 = self.driver.find_element(By.XPATH, value="(//img)[4]")
        action.move_to_element(user3).perform()
        r3 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h5[text()='name: user3']")))
        assert r3, "Test Failed"