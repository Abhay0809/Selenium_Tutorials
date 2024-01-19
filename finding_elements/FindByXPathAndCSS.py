from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from TestDrivers import ChromeDriver


class FindByXPathAndCSS():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        chrome_service = ChromeService(
            executable_path=ChromeDriver)
        driver = webdriver.Chrome(service=chrome_service)
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        elementByXPath = driver.find_element(By.XPATH, "//input[@id='name']")
        if elementByXPath is not None:
            print("Element found -> By XPath")

        elementByCSS = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if elementByCSS is not None:
            print("Element found -> By CSS")



run_test = FindByXPathAndCSS()
run_test.test()
