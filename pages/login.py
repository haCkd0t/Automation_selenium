import time

from selenium.webdriver.common.by import By

class Login:
    def __init__(self,driver):
        self.driver = driver

    def Login_valid(self):
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.find_element(By.XPATH,value="//input[@name='username']").send_keys("tomsmith")
        self.driver.find_element(By.XPATH,value="//input[@name='password']").send_keys("SuperSecretPassword!")
        self.driver.find_element(By.XPATH,value="//button").click()
        self.driver.implicitly_wait(4)
        assert "You logged into a secure area!" in self.driver.page_source, "Login Failed"

    def Logout(self):
        self.driver.find_element(By.XPATH,"//a[@class='button secondary radius']").click()
        self.driver.implicitly_wait(4)
        assert "You logged out of the secure area!" in self.driver.page_source, "Logout Failed"

    def login_invalid_password(self):
        self.driver.find_element(By.XPATH, value="//input[@name='username']").send_keys("tomsmith")
        self.driver.find_element(By.XPATH, value="//input[@name='password']").send_keys("SuperSecretsword!")
        self.driver.find_element(By.XPATH, value="//button").click()
        time.sleep(3)
        assert "Your password is invalid!" in self.driver.page_source, "Login Failed"
    def login_invalid_username(self):
        self.driver.find_element(By.XPATH, value="//input[@name='username']").send_keys("tith")
        self.driver.find_element(By.XPATH, value="//input[@name='password']").send_keys("SuperSecretsword!")
        self.driver.find_element(By.XPATH, value="//button").click()
        time.sleep(3)
        assert "Your username is invalid!" in self.driver.page_source, "Login Failed"


