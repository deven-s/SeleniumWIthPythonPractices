from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\suryawanshi_de\Downloads\Chromedriver.exe")

#driver.get("http://demo.automationtesting.in/Register.html")

driver.get("https://courses.letskodeit.com/practice")

# How to use id attribute of element to find the element
driver.find_element(By.ID, "carselect").click()
driver.find_element_by_id("carselect").click()





# driver.find_element_by_xpath(".//input[@ng-model='FirstName']").send_keys("Art")
# driver.find_element_by_xpath(".//input[@ng-model='LastName']").send_keys("Craft")
# driver.find_element_by_xpath(".//textarea[@ng-model='Adress']").send_keys(" Down Town CA-42563")
# driver.find_element_by_xpath(".//input[@ng-model='EmailAdress']").send_keys("xyz@gmail.com")
# driver.find_element_by_xpath(".//input[@ng-model='Phone']").send_keys("022 653458")
# driver.find_element_by_xpath(".//label[text()=' Male ']/input[@ng-model='radiovalue']")

