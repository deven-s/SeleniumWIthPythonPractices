from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def launchBrowser():
    # Start the driver
    driver = webdriver.Chrome(executable_path=r"C:\Users\suryawanshi_de\Downloads\Chromedriver.exe")
    return driver


driver = launchBrowser()
# Open URL
driver.get("https://seleniumhq.github.io")

# Setup wait for later
wait = WebDriverWait(driver, 10)

# Store the ID of the original window
original_window = driver.current_window_handle

# Check we don't have other windows open already
assert len(driver.window_handles) == 1

time.sleep(5)

driver.execute_script(
    '''window.open("https://www.google.com", "_blank");''')
driver.close()
time.sleep(5)
# Wait for the new window or tab
# wait.until(EC.number_of_windows_to_be(2))

# Loop through until we find a new window handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        #break
print(driver.title)
print("Closing the browser session")
driver.quit()


