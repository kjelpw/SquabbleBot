#Prune a dictionary file to get just have 5 letter words
import csv
import re

read_file = open('english_words_full.txt', newline='')
words = csv.reader(read_file)

with open('dict.csv', 'w', newline='') as csvfile:
    for w in words:
        #check word length, for spaces, and - symbol
        if len(w[0]) == 5 and not bool(re.search(r'\s', w[0])) and not '-' in w[0] and not '\'' in w[0] and not '/' in w[0]:
            csvfile.write((w[0].lower()) + '\n')
            print(w[0])
