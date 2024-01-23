from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToFrame():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        baseUrl = "https://www.letskodeit.com/practice"
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.execute_script("window.scrollBy(0, 1000);")

        # Switch to frame using ID
        driver.switch_to.frame("courses-iframe")

        # Switch to frame using name
        # driver.switch_to.frame("iframe-name")

        # Switch to frame using numbers
        # driver.switch_to.frame(0)


        time.sleep(3)

        # Search course
        searchBox = driver.find_element(By.XPATH, "//input[@id='search']")
        searchBox.send_keys("python")
        time.sleep(3)

        # Switch back to the parent handle/frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(3)
        driver.find_element(By.ID, "name").send_keys("Test Successful")

        time.sleep(3)
        driver.quit()


ff = SwitchToFrame()
ff.test()