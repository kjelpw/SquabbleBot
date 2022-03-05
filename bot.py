from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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

#ready up
actions = ActionChains(driver)
actions.send_keys('ready')
actions.perform()
actions.send_keys(Keys.RETURN)
actions.perform()

#start guessing words

sleep(5)
driver.close()