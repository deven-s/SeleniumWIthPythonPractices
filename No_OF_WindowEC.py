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
driver = webdriver.Chrome(executable_path=r"C:\Users\Downloads\Chromedriver.exe")
driver.maximize_window()

#  2. Go to website
driver.get("https://courses.letskodeit.com/practice")
print(datetime.now())
print(driver.title)

wait = WebDriverWait(driver, 10)
no_of_windows = len(driver.window_handles)

state = wait.until(expected_conditions.number_of_windows_to_be(no_of_windows))
print(state)

driver.find_element_by_id("opentab").click()

no_of_windows = len(driver.window_handles)
print("number of windows {}= " + str(no_of_windows))

state = wait.until(expected_conditions.number_of_windows_to_be(no_of_windows))
print(state)

driver.close()
