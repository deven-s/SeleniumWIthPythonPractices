from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()

# 1 Navigate to url
driver.get("https://www.lambdatest.com/selenium-automation")

# 2. perform explicit wait till the time all the elements in the DOM are available
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//div[text()='CI/CD Tools']/following-sibling::div//a")))

# 3. Go CI-CD and open the url in new tab verify that the same link has been opened.
CICD_url = driver.find_element_by_xpath(".//div[text()='CI/CD Tools']/following-sibling::div//a")
print(CICD_url.get_attribute("href"))


driver.close()