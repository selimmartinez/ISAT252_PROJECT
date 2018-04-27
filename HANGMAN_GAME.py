#HANGMAN_GAME.py
# 

import random

def main():
    welcome = ["Welcome to Hangman!"
                "\nWe will be generating random words for you to guess."
                "\nYou will guess a letter and will have up to 11 guesses."
                "\nor else little Jimmy will be doomed. Goodluck! :)"
               ]


    play_again = True

    while play_again:
        

        wordList = ["python", "java", "integrated", "socializer"
                 "pythonian", "benton", "pneumonoultramicroscopicsilicovolcanoconiosis", 
                 "javascript", "programming", "computer", "carrier", "quiz", "luxembourg"
                 "boat", "solipsism", "jazz", "rhythm"]

        secret_word = random.choice(wordList).lower()
        player_guess = None 
        guessed_letters = [] 
        word_guessed = [] 
        letter_storage = None 

        HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")

        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1

        for letter in secret_word:
            word_guessed.append("-")

        while (attempts != 0 and "-" in word_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            letter_storage = "".join(word_guessed)
            print(letter_storage)

            try:
                player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
            except:
                print("That is not valid input. Please try again.")
                continue                
            else: 
                if not player_guess.isalpha(): 
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess) > 1: 
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess in guessed_letters: 
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass

            guessed_letters.append(player_guess)
 
            for letter in range(len(secret_word)):
                if player_guess == secret_word[letter]:
                    word_guessed[letter] = player_guess 
                    
            if player_guess not in secret_word:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in word_guessed: 
            print(("\nCongratulations! {} was the word").format(secret_word))
        else: 
            print(("\nSorry! The word was {}. Poor Jimmy gets it!").format(secret_word))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if __name__ == "__main__":
    main()