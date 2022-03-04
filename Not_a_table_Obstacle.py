from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://obstaclecourse.tricentis.com/Obstacles/64161/retry#")

driver.find_element_by_id("generate").click()

order_id = driver.find_element_by_xpath(".//div[text()='order id']/following-sibling::div").text

driver.find_element_by_id("offerId").send_keys(order_id)
