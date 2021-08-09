#Simple assignment
from selenium.webdriver import Chrome


# Command to launch the broswer
driver = Chrome(executable_path=r'C:\Users\suryawanshi_de\Downloads\chromedriver.exe')

# Command to navigate to the website or URL
#driver.get("https://selenium.dev")
driver.get(r"C:\Users\suryawanshi_de\Desktop\dropdownlist.html")

# Command to maximize the browser
print(driver.maximize_window)   # This line will do nothing but it will print the method binding with Webdriver class
driver.maximize_window()

  
 # Below 2 lines will open new browser with the Url PASSED parameter to the ger function 
# driver = Chrome(executable_path=r'C:\Users\suryawanshi_de\Downloads\chromedriver.exe')
# driver.get("https://www.selenium.dev/documentation/en/webdriver/understanding_the_components/")

# Command to get the current url from address bar of the browser
print(driver.current_url)
driver.current_url

# command to navigate to previous page
driver.back()

# command to move forward fron browser history
driver.forward()

# command to refresh the page 
driver.refresh()

# command to get the title of page
print("This is title of page - " + driver.title)

# command to get the handle of the window
print(driver.current_window_handle)
