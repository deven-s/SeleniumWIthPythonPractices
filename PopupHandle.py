from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions  # as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
wait = WebDriverWait(driver, 10)

def webde_reg():

    driver.get('https://icodrops.com/ico-stats/')
    #wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, 'permission-core-iframe')))
    driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[@id='save-all-conditionally']")))
    consent_button = driver.find_element(By.ID, 'save-all-conditionally')
    consent_button.click()
    driver.switch_to.default_content()


webde_reg()