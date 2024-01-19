from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetText():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        openTabElement = driver.find_element(By.ID, "opentab")
        elementText = openTabElement.text
        print("Text on element is: " + elementText)

        time.sleep(1)

        driver.quit()

ff = GetText()
ff.test()