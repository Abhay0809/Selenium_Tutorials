from selenium import webdriver
from selenium.webdriver.common.by import By
import time

baseUrl = "https://www.goibibo.com/flights/?utm_source=google&utm_medium=cpc&utm_campaign=DF-Brand-EM&utm_adgroup=Only%20Goibibo&utm_term=!SEM!DF!G!Brand!RSA!108599293!6504095653!617695092667!e!goibibo!c!&gad_source=1&gclid=Cj0KCQiAwbitBhDIARIsABfFYIIrhWCqdTw-bJ-MCobkAOM5a2uV4ySTJI-HBtszg5mZsAc8rB3fx8oaAgRXEALw_wcB"

driver = webdriver.Firefox()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(10)

partialText = "Del"
textToSelect = "New Delhi, India (DEL)"

closeElement = driver.find_element(By.XPATH, "//span[@class='logSprite icClose']")
closeElement.click()

textElement1 = driver.find_element(By.XPATH, "//p[@class='sc-12foipm-20 bhnHeQ']")
textElement1.click()
textElement2 = driver.find_element(By.XPATH, "//input[@type='text']")
textElement2.click()
time.sleep(2)
textElement2.send_keys(partialText)

cityElement = driver.find_element(By.XPATH, "//li[@class='sc-12foipm-41 ehhpAW active']//span[contains(@class,'autoCompleteTitle')]")
inner_html = cityElement.get_attribute('innerHTML')
print(inner_html)




time.sleep(3)
driver.quit()


