from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path=r"C:\Users\Downloads\Chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.expedia.com")


linkElement  = driver.find_element(By.LINK_TEXT,"Expedia.co.in")
partialLinkText = driver.find_element(By.PARTIAL_LINK_TEXT,'Expedia')

print("print partilly identified link")
print(partialLinkText.get_attribute('href'))

print(linkElement.get_attribute('href'))
