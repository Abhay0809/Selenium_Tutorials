from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class WindowSize():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        baseUrl = "https://www.letskodeit.com/practice"
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height: " + str(height))
        print("Width: " + str(width))

        time.sleep(3)
        driver.quit()


ff = WindowSize()
ff.test()