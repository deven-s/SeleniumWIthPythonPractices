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

# driver.find_element_by_xpath(".//button[@onclick='alertbox()']").click()
wait = WebDriverWait(driver, 25)

# testing of expected conditions alert is present
# alert = wait.until(expected_conditions.alert_is_present())
# print(alert.text)

#Checkbox_element = driver.find_element_by_xpath(".//input[@value='Cricket']")
#Checkbox_element.click()

# expected condition checking attribute of the element
# state = wait.until(expected_conditions.element_located_selection_state_to_be((By.XPATH, ".//label[text()=' Male ']/input"), True))

# expected condition to check whether located element is selected
# state = wait.until(expected_conditions.element_located_to_be_selected((By.XPATH,".//input[@value='Cricket']")))

# expected condition to check whether the element is selected ( difference this method does not accept the locator)
# state = wait.until(expected_conditions.element_selection_state_to_be(Checkbox_element, True))

# Expected condition to check whether the element is selected
# state = wait.until(expected_conditions.element_to_be_clickable([By.XPATH, ".//h2[text()='Register']"]))

#radio_btn = driver.find_element_by_xpath(".//input[@value='FeMale']")
#radio_btn.click()

#state = wait.until(expected_conditions.element_to_be_selected(radio_btn))
#print(state)

# expected condition to check iframe, if available switch to it otherwise timeout exception
#state = wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.XPATH, ".//iframe[@name = 'SingleFrame']")))

# use this site to test below functions - https://courses.letskodeit.com/practice
# check visibility of element using expected condition

# click on hide button
driver.find_element(By.XPATH, ".//input[@onclick='showElement()']").click()
#time.sleep(5)

# state = wait.until(expected_conditions.invisibility_of_element((By.XPATH, ".//input[@style='display: block;']")))

########################       new window open scenario     ####################################

# win_handle = driver.window_handles
# print(win_handle)
# state = wait.until(expected_conditions.invisibility_of_element_located((By.XPATH, ".//input[@style='display: block;']")))

# driver.execute_script('''window.open("https://www.google.com", "_blank");''')
# print(driver.current_window_handle)
# state = wait.until(expected_conditions.new_window_is_opened(win_handle))

# print(state)
###############################################################################################
# Difference between find_elements and find_element
# This will return first matching element even if locator matches are more than 1 element, will raise an exception if
# element is not found

# element = driver.find_element(By.XPATH, ".//input[starts-with(@id,'checkbox')]")
# print(element)

# this will return list if elements found else will return empty list, and will not raise any exceptions
# element_list = driver.find_elements(By.XPATH, ".//input[starts-with(@id,'checkbox')]")
# print(element_list)

# for i in element_list:
    # i.click()
    # print(i.find_element(By.XPATH, ".//following-sibling::label").text)
##########################################################################################################

driver.close()
