from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.get('https://app.powerbi.com/view?r=eyJrIjoiMDMzMTcxZGEtMjlhNy00NzQzLThlZDMtY2QxZDg3ZTZjYmY5IiwidCI6IjM5NTgyOTkyLTNiMmUtNDliMS05MTRkLTk0MTJhYzYxNDU5YiIsImMiOjh9')
sleep(2)

popup = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div')
popup.style = 'display: none'
sleep(1)

tweet = driver.find_element_by_css_selector(r'#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > section > div > div')
tweet.screenshot('test_tweet.png')