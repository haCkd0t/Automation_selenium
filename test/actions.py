from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
from selenium.webdriver import ActionChains

def Add_element(driver, wait):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    driver.find_element(By.XPATH, value="//button[@onclick='addElement()']").click()
    dlt = driver.find_element(By.XPATH, value="//button[@class='added-manually']").text
    return dlt


def Dlt_element(driver, wait):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    driver.find_element(By.XPATH, value="//button[@onclick='addElement()']").click()
    driver.implicitly_wait(3)
    delete_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "added-manually")))
    delete_button.click()
    is_gone = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "added-manually")))
    return is_gone


def broken_img(driver, wait):
    driver.get("https://the-internet.herokuapp.com/broken_images")
    img_elements = driver.find_elements(By.XPATH, "//div/img")

    results = []
    for img in img_elements:
        url = img.get_attribute("src")
        response = requests.get(url)
        results.append((url, response.status_code))
    return results


def check_box(driver, wait):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    driver.find_element(By.XPATH, value="(//input[@type='checkbox'])[1]").click()
    box_1 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]")
    box_2 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")
    if (box_2.is_selected and box_1.is_selected):
        return True
    else:
        return False


def right_click_alert(driver, wait):
    ac = ActionChains(driver)
    driver.get("https://the-internet.herokuapp.com/context_menu")
    driver.implicitly_wait(3)
    element = driver.find_element(By.XPATH, value="//div[@id='hot-spot']")
    ac.context_click(element).perform()
    alert = driver.switch_to.alert
    wait.until(EC.alert_is_present())
    t = alert.text
    return t

def drag_drop(driver,wait):
    ac = ActionChains(driver)
    drag = driver.find_element(By.XPATH,)
