#hangman.py

import random

print("Welcome to Hangman!" 
		"\nWe will be generating random words for you to guess."
		"\nYou will guess a letter and will have up to 6 lives" 
		"\nor else little Jimmy will be doomed. GOOD LUCK!")

WORDS = ("hello c", "pythonian", "javascripter", "boolean", "hello world", 
		"code reader", "socializer", "commando", "caffeinator", "sublime")
word = random.choice(WORDS)

def pick_word():
	return "pythonian"

