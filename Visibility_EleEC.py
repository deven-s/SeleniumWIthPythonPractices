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
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#driver = webdriver.Chrome(executable_path=r"C:\Users\suryawanshi_de\Downloads\Chromedriver.exe")
driver.maximize_window()

#  2. Go to website
driver.get("https://courses.letskodeit.com/practice")
print(datetime.now())
print(driver.title)

element = driver.find_element_by_name("show-hide")

wait = WebDriverWait(driver, 10)
# checks for element visibility with height and width and returns same element once it is visible
# visible_state = wait.until(expected_conditions.visibility_of(element))

##############################################################################################################
# check the visibility of all the matching elements and return the list of it
visible_elements_list = wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, ".//select[@name='multiple-select-example']/option[last() and preceding-sibling::option]")))

# print(str(visible_state))
for result in visible_elements_list:
    print(result) #.__getattribute__("value"))
    print(result.get_attribute("value"))

##########################################################################################################################

driver.find_element_by_xpath(".//input[@value='Hide']").click()
time.sleep(5)

element_list = wait.until(expected_conditions.visibility_of_any_elements_located((By.XPATH, ".//input[@name='show-hide' or @value='Show']")))



print(element_list[0].get_attribute("id"))

#############################################################################################################


wait.until()

driver.close()