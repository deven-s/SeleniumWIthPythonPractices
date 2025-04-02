from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common import actions
import time
from selenium.common.exceptions import StaleElementReferenceException

# 1.  Launch/Instantiate the chrome browser
driver = webdriver.Chrome(executable_path=r"C:\Users\Downloads\Chromedriver.exe")
driver.maximize_window()

#  2. Go to website
driver.get("https://courses.letskodeit.com/practice")
print(datetime.now())


wait = WebDriverWait(driver, 10)


#

time.sleep(5)
driver.find_element_by_name("enter-name").send_keys("Arrye ohh babua")

#
var2 = wait.until(expected_conditions.text_to_be_present_in_element_value((By.NAME, "enter-name"), 'Arrye ohh babua'))
text = wait.until(expected_conditions.text_to_be_present_in_element((By., ".//h1[@data-uniqid='1621702280245']"), driver.title))

#var2.send_keys("Arrye ohh babua")

print(var2)


driver.close()
text = wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//h1[@data-uniqid='1621702280245']"), driver.title))

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.ui import test
