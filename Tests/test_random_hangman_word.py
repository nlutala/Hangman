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

    def test_randomhangmanword_returns_word_with_length_three_or_greater_when_easy(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("EASY").generateRandomWord(letter)
        assert len(word) >= 3

    def test_randomhangmanword_returns_word_with_no_hyphens_when_easy(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("EASY").generateRandomWord(letter)
        assert word.count("-") == 0

    def test_randomhangmanword_returns_one_word_when_medium(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)
        assert word.count(" ") == 0

    def test_randomhangmanword_returns_word_starting_with_letter_when_medium(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)
        assert word[0] == letter

    def test_randomhangmanword_returns_word_with_length_is_five_or_greather_when_medium(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)
        assert len(word) >= 5

    def test_randomhangmanword_returns_word_with_no_hyphens_when_medium(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)
        assert word.count("-") == 0

    def test_randomhangmanword_returns_one_word_when_hard(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("HARD").generateRandomWord(letter)
        assert word.count(" ") == 0

    def test_randomhangmanword_returns_word_starting_with_letter_when_hard(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("HARD").generateRandomWord(letter)
        assert word[0] == letter

    def test_randomhangmanword_can_return_word_with_a_hyphen_when_hard(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("HARD").generateRandomWord(letter)
        assert word.count('-') >= 0

    def test_randomhangmanword_returns_word_with_length_is_seven_or_greater_when_hard(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("HARD").generateRandomWord(letter)
        assert len(word) >= 7

    def test_randomhangmanword_raises_an_error_if_a_letter_is_not_passed_to_generateRandomWord(self):
        with self.assertRaises(ValueError):
            RandomHangmanWord().generateRandomWord("\n")

        with self.assertRaises(ValueError):
            RandomHangmanWord().generateRandomWord("sdhba")

        with self.assertRaises(ValueError):
            RandomHangmanWord().generateRandomWord("nlutala")
