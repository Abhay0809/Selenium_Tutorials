from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementState:

    def test(self):
        baseUrl = "https://www.google.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        e1 = driver.find_element(By.ID, "APjFqb")
        e1State = e1.is_enabled()  # True for enabled and False for disabled
        print("E1 is enabled? " + str(e1State))

        e1.send_keys("letskodeit")

        driver.quit()


e = ElementState()
e.test()
