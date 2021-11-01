#Assignment on OrangeHRM

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver=webdriver.Chrome(executable_path=r"C:\Users\Downloads\Chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title)

driver.find_element(By.XPATH, ".//div[@id='divUsername']").click() #on username port

driver.find_element(By.XPATH, ".//input[@id='txtUsername']").click() #click on username port
driver.find_element(By.XPATH, ".//input[@id='txtUsername']").send_keys("Admin")#enter a id in user name port
driver.implicitly_wait(8)
driver.find_element(By.XPATH, ".//div[@id='divPassword']")# on password port
driver.find_element(By.XPATH, ".//input[@id='txtPassword']").click() #click on password port
driver.find_element(By.XPATH, ".//input[@id='txtPassword']").send_keys("admin123")#enter a password in password port
driver.implicitly_wait(8)
driver.find_element(By.XPATH, ".//input[@id='btnLogin']").click()

driver.close()
print('my first ever programm done')
