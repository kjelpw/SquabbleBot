from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions
import time

opts = FirefoxOptions()
#opts.add_argument('--headless')
driver = webdriver.Firefox(options=opts)
driver.get('https://squabble.me/')
assert 'Squabble' in driver.title

#start a game
blitz_button = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div[1]')
blitz_button.click()
time.sleep(1)
find_game_button = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div[4]')
find_game_button.click()
time.sleep(1)

#enter anything


driver.close()