'''
Generates a random word starting with a random letter.
'''
from wonderwords import RandomWord

class RandomHangmanWord:
    def __init__(self, level="EASY") -> None:
        '''
        Initialise the RandomHangmanWord object
        with a level (either "EASY", "MEDIUM" or "HARD")
        '''
        self.level = level
        self.word_min_length = 0
        
        if level == "EASY":
            self.word_min_length = 4
        elif level == "MEDIUM":
            self.word_min_length = 7
        else:
            self.word_min_length = 10

    def generateRandomWord(self, random_letter) -> str:
        '''
        Generate a random word starting with a random letter
        '''
        return RandomWord().word(
            starts_with=random_letter,
            word_min_length=self.word_min_length
        )
    