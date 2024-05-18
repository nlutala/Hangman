'''
Test the functionality of the RandomLetter class
'''
import unittest
from random_letter import RandomLetter

class TestRandomLetter(unittest.TestCase):
    def test_randomletter_returns_one_character(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        assert len(letter) == 1

    def test_randomletter_returns_a_letter(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        assert letter.isalpha() == True
