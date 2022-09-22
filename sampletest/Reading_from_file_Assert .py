# Flipkart scenario automation
# This is an interview Question related Programme
# Code by Devendra
# Use of EXPLICIT_WAIT
# Dt.30/08/2021

from selenium.webdriver.common import by
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.flipkart.com/")

wait = WebDriverWait(driver, 15)

# handling a alert using click method
driver.find_element_by_xpath(".//button[@class='_2KpZ6l _2doB4z']").click()
# Electronic=driver.find_element(By.XPATH,"(.//div[@class='_37M3Pb']/div[@class='eFQ30H'])[5]").click()

# click on electronics section
electronic = wait.until(ec.presence_of_element_located((By.XPATH, ".//div[text()='Electronics']")))
actions = ActionChains(driver)
actions.move_to_element(electronic).perform()

# click on laptop accessories
wait.until(ec.visibility_of_element_located((By.XPATH, ".//a[@class='_6WOcW9 _2-k99T']"))).click()

# mouse hover on electronics section
ele2 = wait.until(ec.presence_of_element_located((By.XPATH, ".//span[text()='Electronics']")))
print(ele2.text)
driver.find_element(By.XPATH, ".//span[text()='Electronics']").click()

# find the apple section
apple = wait.until(ec.visibility_of_element_located((By.XPATH, ".//a[@title='Apple']")))
print(apple)

driver.find_element(By.XPATH, ".//a[@title='Apple']").click()

# shop of iphone XR and click on it
href = wait.until(ec.presence_of_element_located((By.XPATH, ".//a[contains(@href,'-xr-')]"))).get_attribute('href')  #click()
driver.get(href)
print(href)

# for ele in xr_iphone:
    #if ele.get_attribute("href").find("xr"):
        #ele.click()

# driver.find_element(By.XPATH, ".//div[@class='qrCnTo']/a[1]").click()
# print(xr_iphone)

# shop the i phone in given list(3rd no. i phone ) you should  click on it
shop = wait.until(ec.presence_of_element_located((By.XPATH, "(.//div[@class='col col-7-12']/div[@class='_4rR01T'])[3]")))
print(shop.text)

driver.find_element(By.XPATH, "(.//div[@class='col col-7-12']/div[@class='_4rR01T'])[3]").click()

print("Successfully shop by Automated")

# Way 1 of asserting value - read model info from file

file1 = open("../readInput.txt", 'r')
contents = file1.read()
print(contents)

assert shop.text == contents

# Way 2 of asserting element -
xpath = ".//div[contains(text(), '" + contents + "')]"
print(xpath)
is_present = driver.find_element_by_xpath(xpath).is_displayed()

assert is_present == True

driver.close()


