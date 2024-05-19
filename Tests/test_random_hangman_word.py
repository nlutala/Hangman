'''
Test the functionality of the RandomHangmanWord class
'''
import unittest
from random_letter import RandomLetter
from random_hangman_word import RandomHangmanWord

class TestRandomHangmanWord(unittest.TestCase):
    def test_randomhangmanword_returns_one_word_when_easy(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("EASY").generateRandomWord(letter)
        assert word.count(" ") == 0

    def test_randomhangmanword_returns_word_starting_with_letter_when_easy(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("EASY").generateRandomWord(letter)
        assert word[0] == letter

    def test_randomhangmanword_returns_word_with_length_no_greater_than_four_when_easy(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("EASY").generateRandomWord(letter)
        assert len(word) <= 4

    def test_randomhangmanword_returns_one_word_when_medium(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)
        assert word.count(" ") == 0

    def test_randomhangmanword_returns_word_starting_with_letter_when_medium(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)
        assert word[0] == letter

    def test_randomhangmanword_returns_word_with_length_no_greater_than_seven_when_medium(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)
        assert len(word) >= 7

    def test_randomhangmanword_returns_one_word_when_hard(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("HARD").generateRandomWord(letter)
        assert word.count(" ") == 0

    def test_randomhangmanword_returns_word_starting_with_letter_when_hard(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("HARD").generateRandomWord(letter)
        assert word[0] == letter

    def test_randomhangmanword_returns_word_with_length_no_greater_than_twenty_when_hard(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("HARD").generateRandomWord(letter)
        assert len(word) >= 10
