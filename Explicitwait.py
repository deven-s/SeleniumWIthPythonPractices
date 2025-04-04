from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Downloads\Chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.expedia.com")
print("we are on line number 8")
btn = driver.find_element(By.XPATH, ".//span[text()='Flights']/parent::a[@class='uitk-tab-anchor']")
clickreturn = btn.click()  # click on flight button
print(clickreturn)

time.sleep(5)
# Enter source of flight
driver.find_element(By.XPATH, ".//button[@aria-label='Going to']").click()
time.sleep(5)
driver.find_element(By.XPATH, ".//input[@id='location-field-leg1-origin']").send_keys("New York")

optionsList = driver.find_elements(By.CSS_SELECTOR, "ul > li > button")
optionsList[3].click()


time.sleep(5)
# Enter destination of flight
driver.find_element(By.XPATH, ".//button[@aria-label='Leaving from']").click()
time.sleep(5)
driver.find_element(By.XPATH , ".//input[@id='location-field-leg1-destination']").send_keys("SFO")
optionsList = driver.find_elements(By.CSS_SELECTOR, "ul > li > button")     # alternative xpath - .//ul[@data-stid='location-field-leg1-origin-results']/li/button
optionsList[3].click()

time.sleep(5)
# Enter Departing date
driver.find_element(By.XPATH, ".//button[@id='d1-btn']").click()            #.send_keys("03/04/2020")

time.sleep(5)
# Enter Returning date
driver.find_element(By.XPATH, ".//button[@id='d2-btn']").click()          #.send_keys("03/09/2020")

# Click on search button
driver.find_element(By.XPATH,".//button[text()='Search']").click()

#frameElement = driver.find_element(xpathiframe)


driver.close()



########################## Element identifiers in selenium-  #####

driver.find_element(By.ID, 'cpce-vac-launch').click()
driver.find_element(By.NAME)
driver.find_element(By.TAG_NAME, "a")
driver.find_element(By.LINK_TEXT,'Expedia.co.in')
driver.find_element(By.PARTIAL_LINK_TEXT,'Expedia')
driver.find_element(By.CSS_SELECTOR)
driver.find_element(By.CLASS_NAME)
driver.find_element(By.XPATH)
driver.find_element(By.CLASS_NAME)

#driver.find_element(By.CLASS_NAME)


