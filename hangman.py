'''
Hangman class which helps reveal the correct placement of letters gradually
'''

# 1. User has a set number of guesses until hangman is drawn
#    (For simplicity, the user can only guess letters and not the whole word)
# 2. After each guess, reduce the amount of guesses the user has left by one
# 3. For every right guess, reveal all the places in the word where the letter is
# 4. For every wrong guess, reveal a piece of the hangman drawing
# 5. The game ends when the user guesses the word or runs out of guesses

# Extra features:
# While playing the game, the user can choose to go back to the home screen and pick to play at a different level

class Hangman:
    def __init__(self) -> None:
        self.correct_letters = set()
        self.incorrect_letters = set()

    def getIncorrectGuesses(self) -> str:
        '''
        Returns the list of letters that the user guessed incorrectly
        '''
        return " ".join(list(self.incorrect_letters))
    
    def _getIndexesOfALetterInAWord(self, word: str, letter: str) -> list:
        '''
        Private function that returns a list of the indices
        of where a letter appears in a word

        Params:
        word (str) - a word
        letter (str) - a letter in (or not in) the word
        '''
        indices = [i for i in range(0, len(word)) if word[i].lower() == letter.lower()]
        return indices
    
    def _checkInputIsLetter(self, letter: str) -> Exception:
        '''
        Raises an error if the letter inputted by the user is not one letter

        Param:
        letter (str) - the letter the player thinks is in the word
        '''
        if len(letter) > 1:
            raise ValueError("Expected one letter only.")
        elif letter == "" or letter == " ":
            raise ValueError("An (empty) space is not a valid input. Expected one letter as input only.")

    def revealCorrectLetters(self, word_to_guess: str, letter: str) -> str:
        '''
        Returns a string revealing the occurences of a letter
        in a word.

        Params:
        word_to_guess (str) - the word the player needs to guess
        letter (str) - the letter the player thinks is in the word
        '''
        self._checkInputIsLetter(letter)

        if letter.lower() in word_to_guess.lower():
            self.correct_letters.add(letter.lower())
        else:
            self.incorrect_letters.add(letter.lower())

        # Just because hard words can have hyphens in them
        if '-' in word_to_guess:
            self.correct_letters.add('-')

        # Split the word into a list of its letters
        word_to_guess = list(word_to_guess)

        revealed_pieces = "_" * len(word_to_guess)
        revealed_pieces = list(revealed_pieces)

        for letter in list(self.correct_letters):
            indicies = self._getIndexesOfALetterInAWord(word_to_guess, letter)
            for i in indicies:
                revealed_pieces[i] = letter

        return "".join(revealed_pieces)
