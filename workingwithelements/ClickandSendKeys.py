from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ClickandSendKeys():

    def test(self):
        baseUrl = "https://www.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        loginLink = driver.find_element(By.XPATH, "//a[@href='/login']")
        loginLink.click()

        emailField = driver.find_element(By.ID, "email")
        emailField.send_keys("test")

        passwordField = driver.find_element(By.ID, "login-password")
        passwordField.send_keys("test")

        time.sleep(3)

        emailField.clear()

        time.sleep(3)

        emailField.send_keys("test")





ff = ClickandSendKeys()
ff.test()
