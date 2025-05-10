import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains


class Drag_drop:

    def __init__(self, driver):
        self.driver = driver
        self.drag_element = (By.XPATH, "//div[@id='column-a']")
        self.drop_element = (By.XPATH, "//div[@id='column-b']")

    def element_visible(self):
        wait = WebDriverWait(self.driver, 5)
        self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        is_dis_1 = wait.until(EC.visibility_of_element_located(self.drag_element))
        is_dis_2 = wait.until(EC.visibility_of_element_located(self.drop_element))
        assert is_dis_1, "1st Element Not Found"
        assert is_dis_2, "2nd Element Not Found"

    def drag_drop(self):
        action = ActionChains(self.driver)
        self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        source = self.driver.find_element(*self.drag_element)
        target = self.driver.find_element(*self.drop_element)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()
        assert source.text == "B", "Failed"
