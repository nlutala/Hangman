'''
Generates a random letter from a-z
'''
from random import Random

class RandomLetter:
    def __init__(self) -> None:
        self.letters = "abcdefghijklmnopqrstuvwxyz" 

    def generateRandomLetter(self) -> str:
        index = Random().randint(0, len(self.letters)-1)
        return self.letters[index]