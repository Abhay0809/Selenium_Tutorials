from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class Sliders():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        baseUrl = "https://jqueryui.com/slider/"
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, "//div[@id='slider']//span")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 100, 0).perform()
            print("Sliding element successful")
            time.sleep(2)
        except:
            print("Sliding failed on element")

        time.sleep(3)
        driver.quit()


ff = Sliders()
ff.test()