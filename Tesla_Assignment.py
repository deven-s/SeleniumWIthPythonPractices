from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

# Browser launch
driver = webdriver.Chrome(executable_path=r"C:\Users\suryawanshi_de\Downloads\Chromedriver.exe")
driver.maximize_window()

# get the url
wait = WebDriverWait(driver, 20)
driver.get("https://www.reddit.com/")

# searching for gaming
driver.find_element(By.XPATH, ".//input[@id='header-search-bar']").send_keys("gaming")

# Enter when your search for gaming
ele = driver.find_element(By.XPATH, ".//input[@id='header-search-bar']").send_keys(Keys.ENTER)

# Title of the page
print("title of the")
title = driver.title
print(title)
print("we got a title of the page")

# click on login
button=driver.find_element_by_xpath(".//a[text()='Log In']")
driver.execute_script("arguments[0].click();", button)

# enter a id ,psd and press a login button
iframe=driver.find_element(By.XPATH, ".//iframe[@class='_25r3t_lrPF3M6zD2YkWvZU']")
driver.switch_to.frame(iframe)

# enter a id
ele = driver.find_element_by_xpath("//input[@id='loginUsername']")
ele.send_keys("_sunil_1993")

# enter a password
driver.find_element(By.XPATH, ".//input[@id='loginPassword']").send_keys("Sunil@1993")
driver.find_element(By.XPATH, ".//button[@class='AnimatedForm__submitButton m-full-width']").click()

# upvote and down vote checking
upvote_btn = wait.until(ec.

                        presence_of_element_located((By.XPATH, "(.//div[@data-testid='post-container'])[2]/div//button[starts-with(@id, 'upvote-button-')]")))
# upvote_btn = driver.find_element_by_xpath("(.//div[@data-testid='post-container'])[2]/div//button[starts-with(@id, 'upvote-button-')]")
print(upvote_btn)
upvote_btn.click()