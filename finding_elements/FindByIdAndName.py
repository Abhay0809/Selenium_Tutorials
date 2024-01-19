from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from TestDrivers import ChromeDriver


class FindByIdAndName():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        chrome_service = ChromeService(
            executable_path=ChromeDriver)
        driver = webdriver.Chrome(service=chrome_service)

        # driver.get(baseUrl)
        # driver.implicitly_wait(10)
        #
        # elementById = driver.find_element(By.ID, "displayed-text")
        # if elementById is not None:
        #     print("Element found -> By ID")
        #
        # elementByName = driver.find_element(By.NAME, "show-hide")
        # if elementByName is not None:
        #     print("Element found -> By Name")

        driver.get("https://www.google.com/")
        elementByClass = driver.find_element(By.CLASS_NAME, "lnXdpd")
        if elementByClass is not None:
            print("Element found -> By Class Name")

run_test = FindByIdAndName()
run_test.test()
