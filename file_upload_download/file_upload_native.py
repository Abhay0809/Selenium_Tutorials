from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class NativeFileUpload():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        # baseUrl = "https://www.plupload.com/examples/"
        baseUrl = "https://imgbb.com/upload"
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        # element = driver.find_element(By.XPATH, "//a[@id='uploader_browse']")
        # element = driver.find_element(By.XPATH, "//div[@class='plupload_wrapper']//input[@id='uploader_count']")
        element = driver.find_element(By.XPATH, "//input[@type='file']")

        time.sleep(3)
        element.send_keys("C:\\Users\\Abhay_Anand\\PycharmProjects\\SeleniumWDTutorial\\advanced\\test.png")

        time.sleep(3)
        driver.quit()


ff = NativeFileUpload()
ff.test()