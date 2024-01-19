from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DynamicXPathFormat():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)

        # Login -> Lecture: "How to click and type on a web element"
        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        email = driver.find_element(By.XPATH, "//input[@id='email']")
        email.send_keys("abhay@mailinator.com")
        password = driver.find_element(By.XPATH, "//input[@id='login-password']")
        password.send_keys("Abhay@0809")
        driver.find_element(By.XPATH, "//button[@id='login']").click()

        time.sleep(3)

        # Search for courses -> Lecture: "How to find elements by XPATH in Selenium"
        # driver.find_element(By.XPATH, "//a[@href='/courses']").click()
        driver.find_element(By.XPATH, "//a[contains(text(), 'ALL COURSES')]").click()
        searchBox = driver.find_element(By.XPATH, "//input[@id='search']")
        searchBox.send_keys("JavaScript")

        # Select course -> Lecture: "How to find elements by XPATH in Selenium"
        _course = "//div[@id='course-list']//h4[contains(text(), '{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()

        time.sleep(3)
        driver.quit()


ff = DynamicXPathFormat()
ff.test()

