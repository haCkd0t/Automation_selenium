from selenium.webdriver.common.by import By
import time
import os
class download:
    def __init__(self,driver):
        self.driver = driver

    def Download(self):
        self.driver.get("https://the-internet.herokuapp.com/download")
        div = self.driver.find_elements(By.XPATH,value="//div[@class='example']/a")
        time.sleep(2)
        l = []
        for i in div:
            i.click()
            l.append(i.text)
            time.sleep(2)
        time.sleep(10)
        download_dir = 'C:\\Users\\joke\\Downloads'
        f = 0
        for i in l:
            file = os.path.join(download_dir,i)
            if os.path.isfile(file):
                print(f"{i} is available")
            else:
                f = 1
                print(f"{i} is not Available")

        assert f == 0 , "Test Failed"

