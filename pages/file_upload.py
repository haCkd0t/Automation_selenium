from selenium.webdriver.common.by import By
import time
class upload:
    def __init__(self,driver):
        self.driver = driver

    def Upload(self):
        self.driver.get("https://the-internet.herokuapp.com/upload")
        self.driver.find_element(By.XPATH,value="//input[@id='file-upload']").send_keys("C:\\Users\\joke\\Downloads\\Intern_Certificate.jpg")
        time.sleep(3)
        self.driver.find_element(By.XPATH,value="//input[@class='button']").click()
        time.sleep(2)
        assert "File Uploaded!" in self.driver.page_source, "Test Failed File is not Uploaded"