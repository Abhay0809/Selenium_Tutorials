from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ImplicitWaitDemo():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//a[@href='/login']")
        loginLink.click()

        emailField = driver.find_element(By.ID, "email")
        emailField.send_keys("test")

        time.sleep(1)
        driver.quit()


ff = ImplicitWaitDemo()
ff.test()
