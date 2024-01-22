from selenium import webdriver
from selenium.webdriver.common.by import By
from wait_types.explicit_wait_type import ExplicitWaitTypes
import time


class ExplicitWaitDemo2():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)

        wait = ExplicitWaitTypes(driver)
        element = wait.waitForElement("//a[contains(text(),'Sign In')]", "XPATH")
        element.click()

        time.sleep(2)
        driver.quit()


ff = ExplicitWaitDemo2()
ff.test()