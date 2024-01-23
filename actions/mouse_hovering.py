from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class MouseHovering():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        baseUrl = "https://www.letskodeit.com/practice"
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(3)
        element = driver.find_element(By.ID, "mousehover")
        itemToClickLocator = "//div[@class='mouse-hover-content']//a[text()='Top']"

        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(3)
            topLink = driver.find_element(By.XPATH, itemToClickLocator)
            actions.move_to_element(topLink).click().perform()
            print("Item Clicked")
        except:
            print("Mouse Hover failed on element")

        time.sleep(3)
        driver.quit()


ff = MouseHovering()
ff.test()