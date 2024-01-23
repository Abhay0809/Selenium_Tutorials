from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToWindow():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        baseUrl = "https://www.letskodeit.com/practice"
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        # Find the open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(3)

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                time.sleep(3)
                searchBox = driver.find_element(By.XPATH, "//input[@id='search']")
                searchBox.send_keys("python")
                time.sleep(3)
                driver.close()
                break

        # Switch back to the parent handle
        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID, "name").send_keys("Test Successful")

        time.sleep(3)
        driver.quit()


ff = SwitchToWindow()
ff.test()