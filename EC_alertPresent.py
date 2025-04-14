from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  # as EC
from datetime import datetime

# 1.  Launch/Instantiate the chrome browser
driver = webdriver.Chrome(executable_path=r"C:\Users\Downloads\Chromedriver.exe")
driver.maximize_window()

#  2. Go to Bank Bazaar website
driver.get("http://demo.automationtesting.in/Alerts.html")
print(datetime.now())
print(driver.title)
driver.find_element_by_xpath(".//button[@onclick='alertbox()']").click()
wait = WebDriverWait(driver, 5)

# testing of expected conditions alert is present
alert = wait.until(expected_conditions.alert_is_present())
print(alert.text)

# expected condition cheking attribute of the element
wait.until(expected_conditions.element_located_selection_state_to_be(".//a[@href='#CancelTab']", ))



# open one more browser instance
driver = webdriver.Chrome(executable_path=r"C:\Users\Downloads\Chromedriver.exe") @asd;lfajsrnandom code not relevant
driver.maximize_window()







fake_code = "which does nothing";
