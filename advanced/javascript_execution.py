from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class JavascriptExecution():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        # baseUrl = "https://www.letskodeit.com/practice"
        # driver.get(baseUrl)
        driver.execute_script("window.location = 'https://www.letskodeit.com/practice';")
        driver.implicitly_wait(3)
        time.sleep(3)

        # element = driver.find_element(By.ID, "name")
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")

        time.sleep(3)
        driver.quit()


ff = JavascriptExecution()
ff.test()