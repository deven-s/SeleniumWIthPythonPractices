'''practice on letskode site by pytest framework'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

# creating a set up method and teardown
driver = None
#global driver


def setup_module():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    print("inside setup")


def teardown_module():
    print("inside teardown")
    driver.quite()


# click the button
def test_checkbutton():
    driver.get("https://courses.letskodeit.com/practice")
    driver.find_element_by_id("bmwradio").click()
    #teardown_module()


# click the BMW check Box
def test_checkBox():
    driver.get("https://courses.letskodeit.com/practice")
    driver.find_element_by_id("bmwcheck").click()


#teardown_module()