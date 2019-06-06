# the below chunk of text will strip the new lines from words.txt, import them into a list, and then use random to pull a random word from said list

word_list = [line.rstrip('\n') for line in open("words.txt")]

import random

print("it is a mystery! " + "👻")
print(random.choice(word_list))