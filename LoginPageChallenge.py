from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


#1.  Launch/Instantiat the chrome browser
driver = webdriver.Chrome(executable_path=r"C:\Users\Downloads\Chromedriver")
driver = webdriver.Chrome(executable_path=r"C:\Users\Downloads\Chromedriver.exe")
driver.maximize_window()
driver.minimize_window()

#  2. Go to Bank Bazaar website
driver.get("https://portal.id.cps.edu/idp/AuthnEngine#/authn")
driver.implicitly_wait(5)

loginBox1 = driver.find_element_by_xpath('//input[@id ="identificaton"]')
