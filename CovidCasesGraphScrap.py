from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
# Navigate to url
driver.get("https://www.google.com/search?q=covid+cases+in+india&hl=en&source=hp&ei=DqJBYe2zGZCy5OUP4I2byAY&iflsig=ALs-wAMAAAAAYUGwHtmZfYnzZEFUMgK_zxO0C2sMpTzH&oq=covid+cases+in&gs_lcp=Cgdnd3Mtd2l6EAMYADIICAAQgAQQsQMyCwgAEIAEELEDEIMBMggIABCABBCxAzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIFCAAQgAQyCAgAEIAEELEDMgUIABCABDIICAAQgAQQsQM6CAgAEOoCEI8BOggILhCxAxCDAToLCC4QgAQQxwEQ0QM6BQguEIAEOgoIABCxAxCDARAKOggIABCABBDJAzoFCAAQkgM6CwgAEIAEELEDEMkDOggIABCxAxCDAToHCAAQgAQQCjoHCAAQsQMQCjoKCAAQsQMQyQMQCjoFCAAQsQNQyd-7AljXg7wCYO-JvAJoBHAAeACAAYMFiAHQG5IBCTAuOS41LjUtMZgBAKABAbABCg&sclient=gws-wiz")
actions = ActionChains(driver)

########### 1st graph  ########
# list_of_graph_points = driver.find_elements_by_xpath("(.//*[name()='svg' and @class='uch-psvg'])[position()<2]//*[name()='rect']")

# print(len(list(set(list_of_graph_points))))

# for elem in list_of_graph_points:
  #  actions.move_to_element(elem).perform()
  #  print(driver.find_element_by_class_name("ExnoTd").text)


############# 2nd graph ########################
pointer = driver.find_element_by_xpath(".//div[@jscontroller='PTcbkc']/div[@class='RgSmac']")
actions.move_to_element(pointer).perform()
xcord = pointer.location.get("x")
ycord = pointer.location.get("y")

print(xcord, ycord)

time.sleep(10)
driver.execute_script("arguments[0].setAttribute('style','left: 32px; height: 194px; transform: translate3d(0px, 0px, 0px);')", pointer)
pointer = driver.find_element_by_xpath(".//div[@jscontroller='PTcbkc']/div[@class='RgSmac']")
for i in range(620):
    print(i)
    #driver.execute_script(
      #  "arguments[0].setAttribute('style','left: 32px; height: 194px; transform: translate3d("+str(i)+"px, 0px, 0px);')",
      #  pointer)
    cursor = driver.find_element_by_xpath(".//div[@jscontroller='PTcbkc']/div[@class='RgSmac']")
    actions.move_to_element_with_offset(cursor, i, 0).perform()
    #actions.move_to_element(cursor).perform()
    print(driver.find_element_by_xpath(".//table[@class='swWWne']").text)
    print("-----------------------------------")
