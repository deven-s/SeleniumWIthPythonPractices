from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common import actions
from datetime import datetime
import time
from selenium.common.exceptions import StaleElementReferenceException

# 1.  Launch/Instantiate the chrome browser
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()

#  2. Go to website
driver.get("http://demo.automationtesting.in/Alerts.html")

driver.find_element_by_xpath(".//a[@href='#Textbox']").click()
driver.find_element_by_xpath(".//a[@href='#Textbox2']").clic()

driver.find_element_by_xpath(".//button[@onclick='promptbox()']").click()
driver.find_element_by_xpath(".//button[@onclick='promptbox()']").click()

alert = driver.switch_to.alert

print(alert.text)

alert.send_keys("Rockstar")

#WebDriverWait(driver, 10).until(expected_conditions.alert_is_present())
#WebDriverWait(driver, 10).until(expected_conditions.alert_is_present())
#Alert(driver).send_keys(Keys.CONTROL + X,)

alert.accept()


#
