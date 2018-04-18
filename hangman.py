#hangman.py

import random, sys

wordList = ("helloc", "pythonian", "javascripter", "boolean", "helloworld", 
		"codereader", "socializer", "commando", "caffeinator", "sublime")
guess = []
word = random.choice(wordList)
length = len(word)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

def print_guesses_taken(current: int, total: int) -> None:
	"""Prints how many chances the player has used"""
	print("You are on guess {0}/{6}.".format(current, total))

print("Welcome to Hangman!" 
		"\nWe will be generating random words for you to guess."
		"\nYou will guess a letter and will have up to 6 lives" 
		"\nor else little Jimmy will be doomed. GOOD LUCK!")

print("\nPreparing the secret word...")
for character in word:
		guess.append("-")
print("The secret word you need to guess has", length, "characters")
print("You can only enter 1 letter from a-z\n")
print(guess) 

def guessing():
	

