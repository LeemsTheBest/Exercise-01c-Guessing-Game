#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
#I couldn't figure out how to make it work with non integer answers, but I got it to repeat itself infinitely#
def guessgame() :
    import random
    number = random.randrange(1,11)
    guess = input("I bet you can't guess what number I'm thinking! Here's a hint, it's from 1 to 10. ")
    guess = int(guess)
    guess = int(True)
    if guess == number:
     print("Woah, are you psychic or something? Nice job!")
     print("The number I was thinking of was " + str(number))
    else:
     print("Nice try, but no human can beat an AI!")
     print("The number I was thinking of was actually " + str(number))
     guessgame()
guessgame()
guessgame()
