from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common import actions
from datetime import datetime
import time
from selenium.common.exceptions import StaleElementReferenceException

# 1.  Launch/Instantiate the chrome browser
driver = webdriver.Chrome(executable_path=r"C:\Users\suryawanshi_de\Downloads\Chromedriver.exe")
driver.maximize_window()

#  2. Go to website
driver.get("https://courses.letskodeit.com/practice")
print(datetime.now())
print(driver.title)

wait = WebDriverWait(driver, 10)
# this will check for presence all the elements locator locating                            ## Locator of table values Course and price
element_list = wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, ".//table[@id='product']/tbody/tr/*[position()>1]")))

# this will check for single first matching element presence
element = wait.until(expected_conditions.presence_of_element_located((By.NAME, "enter-name")))
print(element.get_attribute("placeholder"))


# .//table[@id='product']/tbody/tr[(position()<>3) or (position()>3)]/*[position()>2]

# print table content
for element in element_list:
    print(element.text)


driver.close()