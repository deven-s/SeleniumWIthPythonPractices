from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C://Users/devsurya/Downloads/chromedriver.exe")
#driver.implicitly_wait(10) #seconds
driver.get("http://demo.openmrs.org/openmrs/login.htm")
driver.implicitly_wait(10) #seconds
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("Admin123")
driver.find_element_by_id("Pharmacy").click()

driver.find_element_by_id("loginButton").click()

assert "Home" in driver.title

