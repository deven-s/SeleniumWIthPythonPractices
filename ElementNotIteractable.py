from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#chrome_options = Options()

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.thewhiskyexchange.com/")
driver.implicitly_wait(3)

search_bar = driver.find_element(
    By.XPATH, "/html/body/div[3]/nav/div/div[3]/div/div/div[2]/a[2]")
search_bar.click()
driver.implicitly_wait(3)

driver.save_screenshot('./image.png')
driver.quit()