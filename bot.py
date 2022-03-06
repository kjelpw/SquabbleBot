from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import FirefoxOptions
from time import sleep
from wordbank import wordbank
import sys

class game():
    def __init__(self, guesstype):
        #open up firefox
        opts = FirefoxOptions()
        #opts.add_argument('--headless')
        self.driver = webdriver.Firefox(options=opts)
        self.driver.get('https://squabble.me/')
        assert 'Squabble' in self.driver.title
        self.actions = ActionChains(self.driver)

        #start our bank of words
        game_words = wordbank(guesstype)

    def start_game(self):
        #start a game
        blitz_button = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div[1]')
        blitz_button.click()
        sleep(1)
        find_game_button = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div[4]')
        find_game_button.click()
        sleep(1)
        #ready up
        self.send_word('ready')
        self.send_word(Keys.RETURN)

    def send_word(self, text):
        self.actions.send_keys(text)
        self.actions.perform()
        sleep(.25)
    
    def end_game(self):
        sleep(20)
        self.driver.close()

    def guess_next_word(self):
        print('temp')

    def is_game_started(self):
        try:
            health = self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div[1]/div[1]/div').innerHTML
            return True
        except:
            sleep(1)
            print('game not started')
            self.is_game_started()

    def is_game_over(self):
        return False

    def play(self):
        #wait for game to start
        if self.is_game_started():
            print('game started')
        
        while not self.is_game_over():
            #get health of the player
            health = self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div[1]/div[1]/div').innerHTML
            print(health)
            self.guess_next_word()



if __name__ == "__main__" :
    print('starting wordle game')
    print(str(sys.argv[1]))
    mygame = game(str(sys.argv[1]))
    mygame.start_game()

    print('guessing')
    mygame.play()

    print('ending game')
    mygame.end_game()
