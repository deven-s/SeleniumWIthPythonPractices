from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# launch the browser
def LaunchBrowser():
    driver1 = webdriver.Chrome(executable_path=r"C:\Users\Downloads\Chromedriver.exe")
    # maximise the window
    driver1.maximize_window()
    return driver1

driver = LaunchBrowser()

# getting the flipkart URL for testing
driver.get("https://www.flipkart.com/")
wait = WebDriverWait(driver, 5)
#wait.until(EC.title_is(By.XPATH,".//title[contains(text(),'Online Shopping Site for Mobiles, Electronics, Furniture')]"),True)

# getting the flipkart URL for testing
driver.get("https://www.flipkart.com/")
wait = WebDriverWait(driver, 5)
#wait.until(EC.title_is(By.XPATH,".//title[contains(text(),'Online Shopping Site for Mobiles, Electronics, Furniture')]"),True)

print("you have reached to home page")

print("you have reached to home page")

# for closing the popup window after geting the home page of flipkart.com
BtnClose = driver.find_element(By.XPATH, ".//button[@class='_2KpZ6l _2doB4z']")
BtnClose.click()

print("closed the popup window")

# mouse over to electronics link
Action = ActionChains(driver)

move = driver.find_element_by_link_text("Electronics")
Action.move_to_element(move).perform()

# move.click()
print(move)

# click on laptop and desktop link under Electronics
LapDesk = driver.find_element(
    By.XPATH, ".//a[ contains(text(), 'Laptop and Desktop')]")
LapDesk.click()
print("clicked on laptop and desktop link")

# click on Electronics again under Laptop and desktop
#Elector = driver.find_element(By.XPATH, ".//span[@class='_2I9KP_' and text()='Electronics']")
wait.until(EC.presence_of_element_located((By.XPATH, ".//span[text()='Electronics']")))

driver.find_element_by_xpath(".//div[@class='_3Il5oO dwRsDN']//span[text()='Electronics']") .click()

# Elector = driver.find_element_by_link_text("Electronics") // problem coming here
# //*[@id="container"]/div/div[2]/div/div/div/div[1]/a[7]
#

#print blank lines

print()

#Action.move_to_element(dropdown).perform()
wait.until(EC.presence_of_element_located((By.XPATH, ".//a[@title='Apple']")))
driver.find_element_by_xpath(".//a[@title='Apple']").click()
print("click on electronics link now")
# Elector.click()


driver.find_element_by_xpath(".//a[@title='Apple']).click()
