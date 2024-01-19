from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrappers import HandyWrapper
import time


class UsingWrapper():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        hw = HandyWrapper(driver)
        driver.get(baseUrl)

        textField1 = hw.getElement("name")
        textField1.send_keys("Test")

        time.sleep(2)

        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()

        time.sleep(2)
        driver.quit()


ff = UsingWrapper()
ff.test()