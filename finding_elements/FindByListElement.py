from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from TestDrivers import ChromeDriver


class FindByListElement():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        chrome_service = ChromeService(
            executable_path=ChromeDriver)
        driver = webdriver.Chrome(service=chrome_service)
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        elementListByClassName = driver.find_elements(By.CLASS_NAME, "inputs")
        length1 = len(elementListByClassName)

        if elementListByClassName is not None:
            print("ClassName -> Size of the list is: " + str(length1))

        elementListByTagName = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(elementListByTagName)
        if elementListByTagName is not None:
            print("Tag Name -> Size of the list is: " + str(length2))


run_test = FindByListElement()
run_test.test()
