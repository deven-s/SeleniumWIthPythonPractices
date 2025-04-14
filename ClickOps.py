from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("http://demo.automationtesting.in/Register.html")

# Navigate to url
driver.get("http://demo.automationtesting.in/Register.html")


# Store 'google search' button web element
searchBtn = driver.find_element(By.TAG_NAME, "body")
driver.get("http://demo.automationtesting.in/Register.html

# Perform double-click action on the element
#webdriver.ActionChains(driver).double_click(searchBtn).perform()
webdriver.ActionChains(driver).context_click(searchBtn).send_keys(Keys.ARROW_DOWN, Keys.RETURN).perform()
