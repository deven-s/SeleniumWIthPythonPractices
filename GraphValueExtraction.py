from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# Navigate to url
driver.get("http://derivativefind.icicidirect.com/find20/Derivatives/FNOFundFlow/companynfo?compSymbol=VEDL&isIndex=0")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[name()='g' and @clip-path='url(#highcharts-32)']/*[name()='path' and @fill='url(#highcharts-35)']"))).click()

# Store 'google search' button web element
tooltip_data = driver.find_element(By.XPATH, ".//*[name()='g' and @class='highcharts-tooltip' and @zIndex='8']/*[name()='text']")
print(tooltip_data.text)
# Perform double-click action on the element
# webdriver.ActionChains(driver).double_click(searchBtn).perform()
# webdriver.ActionChains(driver).context_click(searchBtn).send_keys(Keys.ARROW_DOWN, Keys.RETURN).perform()

# Perform double-click action on the element
 Perform double-click action on the element
