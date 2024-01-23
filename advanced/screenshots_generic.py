from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Screenshots():

    def test(self):
        baseUrl = "https://www.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Login -> Lecture: "How to click and type on a web element"
        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        email = driver.find_element(By.XPATH, "//input[@id='email']")
        email.send_keys("abhay@mailinator.com")
        password = driver.find_element(By.XPATH, "//input[@id='login-password']")
        # password.send_keys("Abhay@0809")
        password.send_keys("TEST")
        driver.find_element(By.XPATH, "//button[@id='login']").click()
        time.sleep(3)

        self.takeScreenshot(driver)

        time.sleep(3)
        driver.quit()

    def takeScreenshot(self, driver):
        """
        Takes screenshot of the current open web page
        :param driver:
        :return:
        """
        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "C:\\Users\\Abhay_Anand\\PycharmProjects\\SeleniumWDTutorial\\advanced\\"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")


ff = Screenshots()
ff.test()