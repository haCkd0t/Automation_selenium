from pages.dynamic_loading import dyn_loading
import time

def test_dyn_load(driver,wait):
    ob = dyn_loading(driver,wait)
    ob.gif()
    time.sleep(2)
    ob.hello_world()
    time.sleep(2)
    ob.presence_of_element()