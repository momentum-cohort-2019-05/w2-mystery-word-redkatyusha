# the below chunk of text will strip the new lines from words.txt, import them into a list, and then use random to pull a random word from said list

import re
import random
word_list = [line.rstrip('\n') for line in open("words.txt")]
easy_list = [word for word in word_list if len(word) <= 6 and len(word) >= 4]
medium_list = [word for word in word_list if len(word) <= 8 and len(word) >= 6]
hard_list = [word for word in word_list if len(word) <= 12 and len(word) >= 8]
killdozer_list = [word for word in word_list if len(word) > 12]


#words = ['apple', 'cat', 'dog', 'banana','ape']
#filtered_words = [word for word in words if len(word) == 3]

#print("it is a mystery " + "👻")
# print(random.choice(word_list))
# print(random.choice(easy_list))
# print(random.choice(medium_list))
# print(random.choice(hard_list))
# print(random.choice(killdozer_list))


def choose_difficulty(difficulty):
    if difficulty == "e" or difficulty == "E":
        print(random.choice(easy_list))
    elif difficulty == "m" or difficulty == "M":
        print(random.choice(medium_list))
    elif difficulty == "h" or difficulty == "H":
        print(random.choice(hard_list))
    elif difficulty == "k" or difficulty == "K":
        print(random.choice(killdozer_list))
    else:
        print("That's not a difficulty. Try again.")
        difficulty = input("(E)asy, (M)edium, (H)ard, or (K)illdozer Mode? ")
        choose_difficulty(difficulty)


difficulty = input("(E)asy, (M)edium, (H)ard, or (K)illdozer Mode? ")
choose_difficulty(difficulty)