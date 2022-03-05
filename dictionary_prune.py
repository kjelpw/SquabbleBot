#Prune a dictionary file to get just have 5 letter words
import csv
import re

read_file = open('dictionary.csv', newline='')
words = csv.reader(read_file)

write_file = open('dict.csv', 'w')
squabble_words = csv.writer(write_file, delimiter=',')

for w in words:
    #check word length, for spaces, and - symbol
    if len(w[0]) == 5 and not bool(re.search(r'\s', w[0])) and not '-' in w[0]:
        squabble_words.writerow(w[0])
        print(w[0])
