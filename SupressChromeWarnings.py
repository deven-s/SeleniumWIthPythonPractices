from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()

#driver.get("https://letcode.in/shadow")
driver.get("https://pastebin.com/")
time.sleep(10)

# close slide banner
driver.find_element_by_xpath(".//vli[@id='hideSlideBanner']").click()

# accept cookies popup
driver.find_element_by_xpath(".//span[text()='OK, I Understand']").click()

driver.find_element_by_name('PostForm[expiration]').click()

#action = ActionChains(driver)
#action.move_to_element(dropdown).click().perform()
#dropdown.click()
#select = Select(dropdown)
#select.select_by_visible_text('10 Minutes')

driver.find_element_by_id('select2-postform-expiration-result-z0t9-10M').click()
