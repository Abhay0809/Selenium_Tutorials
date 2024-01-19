import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from TestDrivers import ChromeDriver

class RunChromeTests():

    def test(self):

        # Instantiate the FFService

        # Old Syntax
        # driver = webdriver.Chrome(executable_path="C:\\Users\\Abhay_Anand\\PycharmProjects\\SeleniumWDTutorial\\drivers\\chromedriver.exe")

        # New Syntax
        chrome_service = ChromeService(executable_path=ChromeDriver)

        # Instantiate the Firefox browser
        driver = webdriver.Chrome(service=chrome_service)

        # Open the URL
        driver.get("https://www.selenium.dev/")
        time.sleep(5)

run_tests = RunChromeTests()
run_tests.test()
