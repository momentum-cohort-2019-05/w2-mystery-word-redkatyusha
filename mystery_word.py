word_list = [line.rstrip('\n') for line in open("words.txt")]

import random

print(random.choice(word_list))