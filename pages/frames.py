import time

from selenium.webdriver.common.by import By

class frm:
    def __init__(self,driver):
        self.driver = driver

    def frame(self):
        self.driver.get("https://the-internet.herokuapp.com/nested_frames")
        time.sleep(3)
        top_frame = self.driver.find_element(By.XPATH,value="//frame[@name='frame-top']")
        self.driver.switch_to.frame(top_frame)
        left_frame = self.driver.find_element(By.XPATH, value="//frame[@name='frame-left']")
        self.driver.switch_to.frame(left_frame)
        time.sleep(2)
        assert "LEFT" in self.driver.page_source
        time.sleep(2)
        self.driver.switch_to.default_content()
        top_frame = self.driver.find_element(By.XPATH, value="//frame[@name='frame-top']")
        self.driver.switch_to.frame(top_frame)
        middle_frame = self.driver.find_element(By.XPATH, value="//frame[@name='frame-middle']")
        self.driver.switch_to.frame(middle_frame)
        time.sleep(2)
        assert "MIDDLE" in self.driver.page_source
        time.sleep(2)
        self.driver.switch_to.default_content()
        top_frame = self.driver.find_element(By.XPATH, value="//frame[@name='frame-top']")
        self.driver.switch_to.frame(top_frame)
        right_frame = self.driver.find_element(By.XPATH, value="//frame[@name='frame-right']")
        self.driver.switch_to.frame(right_frame)
        time.sleep(2)
        assert "RIGHT" in self.driver.page_source
        time.sleep(2)
        self.driver.switch_to.default_content()
        bttom_frame = self.driver.find_element(By.XPATH, value="//frame[@name='frame-bottom']")
        self.driver.switch_to.frame(bttom_frame)
        time.sleep(2)
        assert "BOTTOM" in self.driver.page_source


