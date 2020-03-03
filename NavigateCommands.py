
##  Description: Demostration of Navigate Commands
#  Author : Devendra S
#  Date: 03-03-2020
#
# #

from selenium import webdriver
# webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\devsurya\Downloads\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

print(driver.title)
time.sleep(5)
driver.get("https://demo.openmrs.org/openmrs/login.htm")
print(driver.title)

driver.back()
print(driver.title)

driver.forward()

print(driver.title)
