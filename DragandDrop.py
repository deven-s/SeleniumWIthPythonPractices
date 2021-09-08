from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\suryawanshi_de\Downloads\Chromedriver.exe")

# Navigate to url
driver.get("https://crossbrowsertesting.github.io/drag-and-drop")

# Store 'box A' as source element
sourceEle = driver.find_element(By.ID, "draggable")

# Store 'box B' as source element
targetEle  = driver.find_element(By.ID, "droppable")

# Performs drag and drop action of sourceEle onto the targetEle
webdriver.ActionChains(driver).drag_and_drop(sourceEle, targetEle).perform()

##########################################################################################
driver.get("http://the-internet.herokuapp.com/drag_and_drop")
driver.maximize_window()
time.sleep(8)
sourceElement = driver.find_element_by_id("column-a")
destinationElement = driver.find_element_by_id("column-b")
#print(driver.find_element_by_id("angular").location, driver.find_element_by_id("droparea").location)
#webdriver.ActionChains(driver).drag_and_drop(sourceElement, destinationElement).perform()
#webdriver.ActionChains(driver).click_and_hold(driver.find_element_by_id("mongo")).pause(4).move_to_element(driver.find_element_by_id("droparea")).release(driver.find_element_by_id("droparea")).perform()

webdriver.ActionChains(driver).click_and_hold(sourceElement).move_to_element(destinationElement).perform()
#Performs release event
webdriver.ActionChains(driver).release().perform()