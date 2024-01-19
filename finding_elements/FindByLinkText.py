from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from TestDrivers import ChromeDriver


class FindByLinkText():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        chrome_service = ChromeService(
            executable_path=ChromeDriver)
        driver = webdriver.Chrome(service=chrome_service)
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        elementByLinkText = driver.find_element(By.LINK_TEXT, "BLOG")
        if elementByLinkText is not None:
            print("Element found -> By Link Text")

        elementByPartialLinkText = driver.find_element(By.PARTIAL_LINK_TEXT, "COURSES")
        if elementByPartialLinkText is not None:
            print("Element found -> By Partial Link Text")



run_test = FindByLinkText()
run_test.test()
