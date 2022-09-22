from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



# 11 - 08 - 2021 
def launchBrowser():
    # Start the driver
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\Downloads\Chromedriver.exe")
    
    return driver


driver = launchBrowser()

# Open URL
driver.get("http://demo.automationtesting.in/Frames.html")

# click on multiple iframe button
driver.find_element_by_xpath(".//a[@href='#Multiple']").click()

# find first iframe1 using xpath
iframe = driver.find_element(By.XPATH, ".//iframe[@src='MultipleFrames.html']")

# switch to first iframe
driver.switch_to.frame(iframe)

# wait before iframe2 loads
driver.implicitly_wait(5)

# find nested iframe2 within iframe1
iframe2 = driver.find_element_by_xpath(".//iframe[@src='SingleFrame.html']")

# switch to iframe2
driver.switch_to.frame(iframe2)

# find the input box using xpath method
inputBox = driver.find_element_by_xpath(
    ".//title[text()='SingleFrame']/ancestor::head/following-sibling::body//input")
print("line no. 24 executing")

# enter text into text box
inputBox.send_keys("ABC")

# Leave the frame zone 
driver.switch_to.default_content()

# click on single frame button
driver.find_element_by_xpath(".//a[@href='#Single']").click()

# wait for last action visibility
driver.implicitly_wait(10)

driver.close()
