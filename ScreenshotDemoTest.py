## This file demonstrates the uses of commands for getting screenshot 
# of element and page of the app under testing

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# 12 - 08 - 2021 
def launchBrowser():
    # Start the driver
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\Downloads\Chromedriver.exe")
    driver.maximize_window()
    
    return driver

driver = launchBrowser()
# Open URL
driver.get("http://demo.automationtesting.in/Frames.html")

# Take screenshot and store it into the current directory
driver.save_screenshot('./image.png')
 
# Take screenshot of element
screenshotBinary = driver.find_element_by_xpath(".//a[@href='#Single']")
print(screenshotBinary.screenshot_as_png)
screenshotBinary.screenshot("./image2.png")


driver.close()

