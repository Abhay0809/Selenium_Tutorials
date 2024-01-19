from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class HiddenElement:

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Find the state of the text box
        textBoxElement = driver.find_element(By.ID, "displayed-text")
        print("Text is visible? " + str(textBoxElement.is_displayed()))  # True if visible, False if not visible
        time.sleep(2)
        # Exception thrown in case element not present in DOM
        # Click the Hide button
        driver.find_element(By.ID, "hide-textbox").click()
        time.sleep(2)

        # Find the state of the text box
        print("Text is visible? " + str(textBoxElement.is_displayed()))
        time.sleep(2)

        # Click the Show button
        driver.find_element(By.ID, "show-textbox").click()
        time.sleep(2)

        # Find the state of the text box
        print("Text is visible? " + str(textBoxElement.is_displayed()))
        time.sleep(2)

        # Browser Close
        driver.quit()

    def testExpedia(self):
        baseUrl = "https://www.expedia.co.in/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.find_element(By.ID, "soft_packages_flight_pill").click()
        d = driver.find_element(By.XPATH, "//button[@aria-label='Leaving from']")
        print("Flights tab clicked: " + str(d.is_displayed()))

        driver.quit()



ff = HiddenElement()
ff.test()
# ff.testExpedia()