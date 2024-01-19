from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService


class RunEdgeTests():

    def test(self):
        # Instantiate the FFService
        edgeservice = EdgeService(
            executable_path="C:\\Users\\Abhay_Anand\\PycharmProjects\\SeleniumWDTutorial\\drivers\\msedgedriver.exe")

        # Instantiate the Firefox browser
        driver = webdriver.Edge(service=edgeservice)
        # Open the URL
        driver.get("https://www.selenium.dev/")


runtests = RunEdgeTests()
runtests.test()
