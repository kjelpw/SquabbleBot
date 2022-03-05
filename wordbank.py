import csv

class wordbank():
    #get our list of words
    def __init__(self):
        read_file = open('dict.csv', newline='')
        words = csv.reader(read_file)

    def get_word(self):
        print('temp')

    def update_position(self, positions):
        print('temp')

    def available_words(self):
        for w in words:
            print(w)