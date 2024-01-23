'''
pip3 install pynput
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time


class FileUpload():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        # baseUrl = "https://www.plupload.com/examples/"
        baseUrl = "https://imgbb.com/upload"
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        # element = driver.find_element(By.XPATH, "//input[@class='plupload_count']")
        element = driver.find_element(By.XPATH, "//a[@data-trigger='anywhere-upload-input']")
        time.sleep(3)
        element.click()
        time.sleep(3)

        keyboard = Controller()

        keyboard.type("C:\\Users\\Abhay_Anand\\PycharmProjects\\SeleniumWDTutorial\\advanced\\test.png")
        time.sleep(3)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(5)
        driver.quit()


ff = FileUpload()
ff.test()