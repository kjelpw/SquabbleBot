from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions
import time

opts = FirefoxOptions()
#opts.add_argument('--headless')
driver = webdriver.Firefox(options=opts)
driver.get('https://squabble.me/')
assert 'Squabble' in driver.title

time.sleep(5)

driver.close()