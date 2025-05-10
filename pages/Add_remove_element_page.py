from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddRemoveElement:
    def __init__(self, driver):
        self.driver = driver
        self.add_element_click = (By.XPATH, "//button[@onclick='addElement()']")
        self.delete_element_click = (By.XPATH, "//button[@class='added-manually']")

    def open_url(self, url):
        self.driver.get(url)

    def verify_Add_button_and_click(self):
        add_button = self.driver.find_element(By.XPATH, value="//button[@onclick='addElement()']")
        assert add_button.is_displayed(), "Add button Not found"
        add_button.click()

    def verify_remove_button_click(self):
        wait = WebDriverWait(self.driver, 5)
        dlt_button = self.driver.find_element(By.XPATH, value="//button[@class='added-manually']")
        assert dlt_button.is_displayed(), "Delete button Not found"
        dlt_button.click()
        is_invisible = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "added-manually")))
        assert is_invisible, "Delete is Visible on screen"
