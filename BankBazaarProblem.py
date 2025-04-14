from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#1.  Launch/Instantiat the chrome browser
driver = webdriver.Chrome(executable_path=r"C:\Users\Downloads\Chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)

#  2. Go to Bank Bazaar website
driver.get("https://www.bankbazaar.com/personal-loan.html")


# 3.  Choose salaried as employee type
element = "(//div[@class='EmploymentType_container_38si1 container-width-for-4-cols']/descendant::input[@name='employmentType'])[1]"
insert = driver.find_element(By.XPATH, element)
insert.click()

# 4. Enter the company name as INFOSYS and select 2nd element from dropdown
driver.find_element(
    By.XPATH, "//input[@placeholder='Start typing here....']").send_keys("INFOSYS")
print("is it enter company name")

# wait for element
    # 4.1 Selecting 2nd value of dropdown for INFOSYS 
dropdown = driver.find_element_by_xpath(".//div[@class='Select-menu-outer']" #.get_attribute("innerHTML")
dropdown.find_element_by_xpath(".//div[@role='listbox']/div[2]").click()


dropdown.find_element_by_xpath(".//div[@role='listbox']/div[2]").click()
# this is non intented comment dropdown.find_element_by_xpath(".//div[@role='listbox']/div[2]").click()
