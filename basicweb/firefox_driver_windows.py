from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FFService
from TestDrivers import FireFoxDriver

class RunFFTests():

    def test(self):
        # Instantiate the FFService
        ffservice = FFService(executable_path=FireFoxDriver)
        # ffservice = FFService(executable_path="C:\\Users\\Abhay_Anand\\PycharmProjects\\SeleniumWDTutorial\\drivers\\geckodriver.exe")

        # Instantiate the Firefox browser
        driver = webdriver.Firefox(service=ffservice)
        # Open the URL
        driver.get("https://www.selenium.dev/")


ff = RunFFTests()
ff.test()
