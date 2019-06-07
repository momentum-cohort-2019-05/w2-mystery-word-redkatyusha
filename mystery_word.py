# the below chunk of text will strip the new lines from words.txt, import them into a list, and then use random to pull a random word from said list

import re
import random
word_list = [line.rstrip('\n') for line in open("words.txt")]
easy_list = [word for word in word_list if len(word) <= 6 and len(word) >= 4]
medium_list = [word for word in word_list if len(word) <= 8 and len(word) >= 6]
hard_list = [word for word in word_list if len(word) <= 12 and len(word) >= 8]
killdozer_list = [word for word in word_list if len(word) > 12]
word = "blah"


print("it is a mystery 👻")


def choose_difficulty(str):
    global word

    if str == "e" or str == "E":
        word = random.choice(easy_list)
    elif str == "m" or str == "M":
        word = random.choice(medium_list)
    elif str == "h" or str == "H":
        word = random.choice(hard_list)
    elif str == "k" or str == "K":
        word = random.choice(killdozer_list)
    elif str == "q" or str == "Q":
        print("Play again later!")
        quit
    else:
        print("That's not a difficulty. Try again.")
        difficulty = input(
            "(E)asy, (M)edium, (H)ard, (K)illdozer, or (Q)uit? ")
        choose_difficulty(difficulty)


def start_over():
    global new_game

    new_game = input("Try again? Y/N: ")
    if new_game == "y" or new_game == "Y":
        difficulty = input("(E)asy, (M)edium, (H)ard, (K)illdozer, or (Q)uit? ")
        choose_difficulty(difficulty)
    elif new_game == "n" or new_game == "N":
        print("Thanks for playing!")
        quit
    else:
        print("Huh? You have pressed an incorrect key.")
        start_over()


difficulty = input("(E)asy, (M)edium, (H)ard, (K)illdozer, or (Q)uit? ")
choose_difficulty(difficulty)

guesses = ""
turns = 8

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You won!")
        start_over()

    guess = input("Guess a character: ") 
    guesses += guess                    

    if guess not in word:  
        turns -= 1        
        print("Wrong...")
 
        print("You have ", turns, " more guesses.")

        if turns == 0:           
            print("You lose! You get nothing! Good day, sir!")
            start_over()