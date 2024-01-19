from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrappers import HandyWrapper
import time



class ElementPresentCheck():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        hw = HandyWrapper(driver)
        driver.get(baseUrl)

        elementResult1 = hw.isElementPresent("name", By.ID)
        print(str(elementResult1))

        elementResult2 = hw.isElementPresent("//input[@id='name']", By.XPATH)
        print(str(elementResult2))

        driver.quit()


ff = ElementPresentCheck()
ff.test()