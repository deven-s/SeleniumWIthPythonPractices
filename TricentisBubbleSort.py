from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()

# Navigate to url
driver.get("https://obstaclecourse.tricentis.com/Obstacles/73589#")


# actions = ActionChains(driver)
def getNumbers():
    bubble_element = driver.find_element_by_class_name("bubble")
    first_num = bubble_element.find_element_by_xpath(".//div[1]").text
    second_num = bubble_element.find_element_by_xpath(".//div[2]").text
    return {"num1": first_num, "num2": second_num}


def clickNextOnTrueCondition():
    if (getNumbers().get("num1")) < (getNumbers().get("num2")):
        driver.find_element_by_id("button2").click()
        print("clicked on next button")
        print("numbers are", getNumbers().get("num1"), getNumbers().get("num2"))
        time.sleep(2)
        clickNextOnTrueCondition()

    elif (getNumbers().get("num1")) > (getNumbers().get("num2")):
        driver.find_element_by_id("button1").click()
        if len(driver.find_elements_by_tag_name("h2")) == 1:
            return "Good Job !!!!"
        else:
            time.sleep(5)
            driver.find_element_by_id("button2").click()
        clickNextOnTrueCondition()


message = clickNextOnTrueCondition()
print(message + "sorting is done")
