from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\Downloads\Chromedriver.exe")
driver.get("https://www.google.com")

#cookie_button = driver.find_element_by_id('L2AGLb')
#cookie_button.click()

search_bar = driver.find_element_by_name("q")
search_bar.clear()

search_bar.send_keys("Taylor Swift")
search_bar.send_keys(Keys.RETURN)

news_button = driver.find_element_by_css_selector('[data-hveid="CAEQAw"]')
news_button.click()

tools_button = driver.find_element_by_id('hdtb-tls')
tools_button.click()

recent_button = driver.find_element_by_class_name('KTBKoe')
recent_button.click()

custom_range_button = dashboards_button = driver.find_elements_by_tag_name('g-menu-item')[6]
custom_range_button.click()

driver.close()
