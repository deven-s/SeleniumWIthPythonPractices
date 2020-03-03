from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path=r"C://Users/devsurya/Downloads/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.expedia.com")
driver.find_element(By.XPATH, ".//button[@data-lob='flight']").click()  # click on flight button

time.sleep(5)
driver.find_element(By.XPATH, ".//input[@id='package-origin-hp-package']").send_keys("New York")
driver.find_element(By.XPATH , ".//input[@id='package-destination-hp-package']").send_keys("SFO")
driver.find_element(By.XPATH, ".//input[@id='package-departing-hp-package']").send_keys("03/04/2020")
driver.find_element(By.XPATH, ".//input[@id='package-returning-hp-package']").send_keys("03/09/2020")

driver.close()