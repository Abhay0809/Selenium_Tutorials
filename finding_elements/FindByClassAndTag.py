import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from TestDrivers import ChromeDriver


class FindByClassAndTag():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        chrome_service = ChromeService(
            executable_path=ChromeDriver)
        driver = webdriver.Chrome(service=chrome_service)
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        elementByClass = driver.find_element(By.CLASS_NAME, "inputs")
        if elementByClass is not None:
            print("Element found -> By Class")
            elementByClass.send_keys("Testing The Element")

        elementByTag = driver.find_element(By.TAG_NAME, "a")
        if elementByTag is not None:
            print("Element found -> By Tag" + elementByTag.text)

        time.sleep(5)


run_test = FindByClassAndTag()
run_test.test()
