from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('C://Users//suryawanshi_de//Desktop//test.html')
#username = driver.find_element_by_id("input-username")
#print(username)
#shadow_root = driver.execute_script('return arguments[0].shadowRoot', username)
lst_ele = driver.find_elements_by_xpath(".//div[@class='offer']")
for i in lst_ele:
    print(i.text)
#shadow_root.find_element_by_xpath('.//div[@id="placeholder"]')
#username.send_keys("stinky_joe123@gmail.com")