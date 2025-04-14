from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
# launch the browser
def LaunchBrowser():
    driver1 = webdriver.Chrome(executable_path=r"C:\Users\Downloads\Chromedriver.exe")
    # maximise the window
    driver1.maximize_window()
    return driver1

driver = LaunchBrowser()

# getting the flipkart URL for testing
driver.get("https://www.google.com/")

driver.find_element_by_xpath(".//input[@name='q']").send_keys("wikipedia.com", Keys.ENTER)
driver.find_element_by_xpath(".//h3[text()='Wikipedia']/parent::a").click()
driver.find_element_by_xpath(".//h3[text()='Wikipedia']/parent::div").click()

driver.find_element_by_id("searchInput").send_keys("Giga Berlin", Keys.ENTER)

coordinates = driver.find_element_by_xpath(".//span[@class='geo-dec']").text

print(coordinates)

co_ord = re.sub("[^0-9.\s]", "", coordinates).replace(" ", ",")
print(co_ord)

driver.find_element_by_xpath(".//span[@class='geo-dec']/ancestor::a").click()

gmap_link = driver.find_element_by_xpath(".//span[text()='Google Maps']/ancestor::a")
gmap_link_href = gmap_link.get_attribute('href')

print(gmap_link_href)

this_window = driver.current_window_handle
gmap_link.send_keys(Keys.CONTROL + Keys.RETURN)

handles = driver.window_handles
for handle in handles:
    if this_window != handle:
        driver.switch_to.window(handle)

text_cord = driver.find_element_by_xpath(".//span[starts-with(text(),'52.4')]").text
print(text_cord)
assert co_ord in gmap_link_href
#driver.close()
