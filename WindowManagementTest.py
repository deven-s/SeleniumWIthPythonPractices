## This file demonstrates the uses of commands for getting window size 
## like width hight

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# 11 - 08 - 2021 
def launchBrowser():
    # Start the driver
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\suryawanshi_de\Downloads\Chromedriver.exe")
    
    return driver

driver = launchBrowser()

# Open URL
driver.get("http://demo.automationtesting.in/Frames.html")
driver.fullscreen_window()

time.sleep(5)
# Get window size or dimensions
width = driver.get_window_size().get("width")
height = driver.get_window_size().get("height")
print(width, height)

driver.set_window_size(1000,400)   #.window().setSize(new Dimension(1024, 768));
#driver.set_window_size(1024, 768)
size = driver.get_window_size()
print("width of browser - "+str(size.get("width")))
print("height of browser -"+str(size.get("height")))


driver.close()