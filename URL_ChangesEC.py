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


url = driver.current_url

#driver.find_element_by_xpath(".//a[text()='HOME']").click()

wait = WebDriverWait(driver, 10)
value = wait.until(expected_conditions.url_changes((url)))

print(value)


#driver.close()