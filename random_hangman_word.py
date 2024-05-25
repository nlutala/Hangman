'''
Generates a random word starting with a random letter.

Nathan Lutala
Github: https://github.com/nlutala
'''
from wonderwords import RandomWord

class RandomHangmanWord:
    def __init__(self, level="EASY") -> None:
        '''
        Initialise the RandomHangmanWord object
        with a level

        Param:
        level (str) - (either "EASY", "MEDIUM" or "HARD")
        '''
        self.level = level
        self.word_min_length = None
        self.regex = None
        
        if level == "EASY":
            self.word_min_length = 3
            self.regex = r'^[^-]*$'
        elif level == "MEDIUM":
            self.word_min_length = 5
            self.regex = r'^[^-]*$'
        else:
            self.word_min_length = 7

    def generateRandomWord(self, random_letter: str) -> str:
        '''
        Generate a random word starting with a random letter

        Param:
        random_letter (str)

        Raises a ValueError if anything but a letter is passed as a parameter
        '''
        if len(random_letter) > 1 or not random_letter.isalpha() or random_letter == "\n":
            raise ValueError("Expected a letter of the alphabet")
        else:
            return RandomWord().word(
                starts_with=random_letter,
                word_min_length=self.word_min_length,
                regex=self.regex
            )
