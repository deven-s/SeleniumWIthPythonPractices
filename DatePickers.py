from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()

#def selectBirthDate(23092021):
def selectReturnJourneyDates():
    allMonthDays = driver.find_elements_by_xpath(".//a[contains(@class,'highlight') or @class='ui-state-default']")
    Today = driver.find_element_by_xpath(".//a[contains(@class,'highlight') ]")
    print(Today)
    print("selecting the departure day and return day")
    #if Today in allMonthDays:
    currentDay = allMonthDays.index(Today)
    print(currentDay)
    departureDay = currentDay + 1
    print(departureDay)

    returnDay = currentDay + 2
    print(returnDay)

    allMonthDays[departureDay].click()
    driver.find_element_by_id("datepicker1").click()
    print("selecting return date")
    allMonthDays[returnDay].click()


# driver.get("http://demo.automationtesting.in/TinyMCE.html")

# driver.find_element_by_tag_name("textarea").send_keys("asdfasdfasdfasdfasdfasdfasdfasdfasdfsadfasdfasdfasdfasdfasdfasdfasdfasdfasfasdfasdasdfasdfasdfasdfasdfasdfasdfasdf")

driver.get("http://demo.automationtesting.in/Datepicker.html")
driver.find_element_by_id("datepicker1").click()
#selectReturnJourneyDates()
