import csv



class wordbank():
    #get our list of words
    def __init__(self, guesstype='bruteforce'):
        self.read_file = open('dict.csv', newline='')
        self.words = csv.reader(self.read_file)

    def get_word(self):
        print('temp')

    def update_position(self, positions):
        print('temp')

    def available_words(self):
        for w in self.words:
            print(w)