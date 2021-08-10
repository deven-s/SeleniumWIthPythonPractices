# Relative locators are introduced in the selenium 4

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import with_tag_name



driver=webdriver.Chrome(executable_path=r"C:\Users\suryawanshi_de\Downloads\Chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
