from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class calendarSection():

    def test1(self):
        baseUrl = "https://www.expedia.co.in/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        # Click on flight tab
        driver.find_element(By.XPATH, "//a[@href='/Flights']/span[contains(text(), Flights)]").click()
        # Find departure field
        departingField = driver.find_element(By.XPATH, "//button[@data-stid='uitk-date-selector-input1-default']")
        # Click on departure field
        departingField.click()
        # Find the date to be selected
        dateToSelect = driver.find_element(By.XPATH, ("//div[@class='uitk-date-selector']//div[@role='application']/div[2]/table[@role='presentation']/tbody/tr[5]/td[4]/div[@role='button']"))

        # Click on the date
        dateToSelect.click()

        time.sleep(10)
        driver.quit()

    def test2(self):
        baseUrl = "https://www.expedia.co.in/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        # Click on flight tab
        driver.find_element(By.XPATH, "//a[@href='/Flights']/span[contains(text(), Flights)]").click()
        # Find departure field
        departingField = driver.find_element(By.XPATH, "//button[@data-stid='uitk-date-selector-input1-default']")

        departingField.click()

        allValidDates = driver.find_elements(By.XPATH, "//div[@class='uitk-date-picker-month']//table[@class='uitk-date-picker-weeks']//tbody//tr//td/button[@class='uitk-date-picker-day uitk-new-date-picker-day']")

        for date in allValidDates:
            if date.text == "30":
                date.click()
                break

        time.sleep(10)
        driver.quit()


ff = calendarSection()
ff.test1()