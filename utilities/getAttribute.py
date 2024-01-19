from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetAttribute():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        element = driver.find_element(By.ID, "name")
        result1 = element.get_attribute("type")
        result2 = element.get_attribute("class")
        print("Value of attribute is: " + result1)
        print("Value of attribute is: " + result2)

        time.sleep(1)
        driver.quit()


ff = GetAttribute()
ff.test()