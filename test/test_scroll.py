import time

from selenium import webdriver

# Initialize the driver
driver = webdriver.Chrome()

# Open your target URL
driver.get("https://demoqa.com/webtables")
driver.maximize_window()

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)