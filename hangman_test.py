#hangman_test.py

#import random 
#print random word:, random.randchar()
from hangman import pick_word

def test_smoke():
	assert True == True

def test_can_pick_random_word():
	assert pick_word() in ["hello c", "pythonian", "javascripter", "boolean", "hello world", 
		"code reader", "socializer", "commando", "caffeinator", "sublime"]

	

