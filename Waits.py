from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


#1.  Launch/Instantiat the chrome browser
driver = webdriver.Chrome(executable_path=r"C:\Users\suryawanshi_de\Downloads\Chromedriver.exe")
driver.maximize_window()

#  2. Go to Bank Bazaar website
driver.get("file:///C:/Users/suryawanshi_de/Desktop/race_condition.html")
driver.implicitly_wait(5)

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.title_is("selenium"))

el = driver.find_element(By.TAG_NAME, "p")
assert el.text == "Hello from JavaScript!"