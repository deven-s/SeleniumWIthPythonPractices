# Description - Selenium Basic Commands
# Author : Devendra S
# Date 03-03-2020
#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path=r"C:\Users\Downloads\chromedriver.exe")
    
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)  # returns title of the page
print(driver.current_url) # return urls of current page

driver.find_element_by_xpath(".//button[text()='    click   ']").click()
time.sleep(5)
driver.close()  # closes current focused window
#driver.quit()
 #test comment
