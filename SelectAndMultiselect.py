from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def selectMultipleLanguages(*args):
    languages_ele = driver.find_elements_by_xpath(".//ul[contains(@class,'ui-menu')]/li")
    if len(languages_ele) > 0:
        languages_ele[args[0]].click()
        languages_ele[args[1]].click()
        languages_ele[args[2]].click()

def selectValueFromDropdown(indexOfItemTobeSelected, xpath_locator):
    Select(driver.find_element_by_xpath(xpath_locator)).select_by_index(indexOfItemTobeSelected)


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()

action = ActionChains(driver)

# Fill the input fields of registration form
driver.find_element_by_xpath(".//input[@ng-model='FirstName']").send_keys("Art")
driver.find_element_by_xpath(".//input[@ng-model='LastName']").send_keys("Craft")
driver.find_element_by_xpath(".//textarea[@ng-model='Adress']").send_keys(" Down Town CA-42563")
driver.find_element_by_xpath(".//input[@ng-model='EmailAdress']").send_keys("xyz@gmail.com")
driver.find_element_by_xpath(".//input[@ng-model='Phone']").send_keys("0653224581")
driver.find_element_by_xpath(".//label[text()=' Male ']/input[@ng-model='radiovalue']").click()
driver.find_element_by_xpath(".//input[@value='Cricket']").click()

print(driver.find_element_by_xpath(".//input[@value='Cricket']").is_selected())

# Get active element in the view
print(driver.switch_to.active_element.get_attribute("value"))

#############################################################################################
# This is multiselect using action class

dd_ele = driver.find_element_by_id("msdd")
# action.move_to_element(dd_ele).click()

# languages_ele = driver.find_elements_by_xpath(".//ul[contains(@class,'ui-menu')]/li")
# print(len(languages_ele))

# multiselect = action.click(languages_ele[1]).click(languages_ele[2]).click(languages_ele[21]).perform()
# print(multiselect)

################################################################################################
# Select class to select dropdown values

select_skill = driver.find_element_by_xpath(".//select[@ng-model='Skill']")
select_items = Select(select_skill)

time.sleep(3)
select_items.select_by_index(1)
time.sleep(3)
select_items.select_by_value("Android")
time.sleep(3)
select_items.select_by_visible_text("C")

print(select_items.options)
######################################################################################################
dd_ele.click()

# Reuse of code by defining methods for repetitive tasks.
selectMultipleLanguages(1, 30, 21)
selectValueFromDropdown(10, xpath_locator=".//select[@ng-model='Skill']")
selectValueFromDropdown(8, xpath_locator=".//select[@id='countries']")


driver.find_element_by_id("imagesrc").send_keys(r"C:\Users\suryawanshi_de\Downloads\Screenshot_20210519-152307_Zomato.jpg")
driver.find_element_by_id("submitbtn").click()

# driver.close()