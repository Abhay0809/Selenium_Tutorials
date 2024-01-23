from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToAlert():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        baseUrl = "https://www.letskodeit.com/practice"
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.find_element(By.ID, "name").send_keys("Test")
        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(3)
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(3)
        driver.find_element(By.ID, "name").send_keys("Test")
        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(3)
        alert2 = driver.switch_to.alert
        alert2.dismiss()


        time.sleep(3)
        driver.quit()


ff = SwitchToAlert()
ff.test()