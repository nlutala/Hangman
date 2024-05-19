'''
Defines the flow of the game
'''

# In a loop a until the user quits the game
# 1. User specifies the mode the level they want to play at (EASY, MEDIUM or HARD)
# 2. Generate a random word according to the level specified
# 3. User has a set number of guesses until hangman is drawn
# 4. For simplicity, the user can only guess letters and not the whole word
# 5. After each guess, reduce the amount of guesses the user has left by one
# 6. For every right guess, reveal all the places in the word where the letter is
# 7. For every wrong guess, reveal a piece of the hangman drawing
# 8. The game ends when the user guesses the word or runs out of guesses

# Extra features:
# While playing the game, the user can choose to go back to the home screen and pick to play at a different level
