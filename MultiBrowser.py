from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


cap = DesiredCapabilities().FIREFOX
cap["marionette"] =     False
#driver = webdriver.Chrome(executable_path=r"C:\Users\Downloads\chromedriver.exe")
driver = webdriver.Firefox(capabilities = cap, executable_path=r"C:\Users\Downloads\geckodriver.exe")
driver.get("https://google.com")

print(driver.title) # title of homepage
driver.close()  #close browser
