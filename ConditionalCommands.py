##
# Description : use of is_displayed() , is_selected() and is_enabled() methods
# Author :  Devendra
# Date : 03-03-2020
#
# #


from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\devsurya\Downloads\chromedriver.exe")

driver.get("http://demo.openmrs.org/openmrs/login.htm")

ele = driver.find_element_by_id("username")

print(ele.is_displayed())  # RETURN true/false based on element status
print(ele.is_enabled())  # Return true if element is enabled
print(ele.is_selected()) # Return true if element is checkbox/radiobutton selected

passfield = driver.find_element_by_id("password")

ele.send_keys("admin")
passfield.send_keys("Admin123")
driver.find_element_by_id('Pharmacy').click()
driver.find_element_by_xpath(".//input[@id = 'loginButton']").click()
print(driver.title)

driver.close()