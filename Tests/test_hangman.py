'''
Test the functionality of the Hangman class
'''
import unittest
from hangman import Hangman
from random_hangman_word import RandomHangmanWord
from random_letter import RandomLetter

class TestHangman(unittest.TestCase):
    def test_hangman_returns_a_string_with_underscores_if_a_letter_is_not_in_the_word(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord().generateRandomWord(letter)
        hangman = Hangman()

        # I chose an arbitrary letter (in this case the letter z)
        string = hangman.revealCorrectLetters(word, 'z')
        
        if 'z' not in string:
            assert string == '_' * len(word)
        else:
            assert 'z' in string

    def test_hangman_returns_a_string_with_the_same_length_as_the_word_to_guess(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord().generateRandomWord(letter)
        hangman = Hangman()

        # I chose an arbitrary letter (in this case the letter v)
        string = hangman.revealCorrectLetters(word, 'v')
        
        assert len(string) == len(word)
