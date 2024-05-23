'''
Test the functionality of the Hangman class
'''
import unittest
from hangman import Hangman
from random_hangman_word import RandomHangmanWord
from random_letter import RandomLetter

class TestHangman(unittest.TestCase):
    def test_hangman_returns_a_string_with_underscores_if_a_letter_is_not_in_the_word_when_easy(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("EASY").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter z)
        string = Hangman().revealCorrectLetters(word, 'z')
        
        if 'z' not in string:
            assert string == '_' * len(word)
        else:
            assert 'z' in string

    def test_hangman_returns_a_string_with_the_same_length_as_the_word_to_guess_when_easy(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("EASY").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter v)
        string = Hangman().revealCorrectLetters(word, 'v')
        
        assert len(string) == len(word)

    def test_hangman_returns_a_string_without_hyphens_if_the_word_is_easy(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("EASY").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter e)
        string = Hangman().revealCorrectLetters(word, 'e')
        
        assert '-' not in string

    def test_hangman_returns_a_string_with_underscores_if_a_letter_is_not_in_the_word_when_medium(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter x)
        string = Hangman().revealCorrectLetters(word, 'x')
        
        if 'x' not in string:
            assert string == '_' * len(word)
        else:
            assert 'x' in string

    def test_hangman_returns_a_string_with_the_same_length_as_the_word_to_guess_when_medium(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter b)
        string = Hangman().revealCorrectLetters(word, 'b')
        
        assert len(string) == len(word)

    def test_hangman_returns_a_string_without_hyphens_if_the_word_is_medium(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter g)
        string = Hangman().revealCorrectLetters(word, 'g')
        
        assert '-' not in string

    def test_hangman_returns_a_string_with_underscores_if_a_letter_is_not_in_the_word_when_hard(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("HARD").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter q)
        string = Hangman().revealCorrectLetters(word, 'q')
        
        if 'q' not in string:
            assert string == '_' * len(word)
        else:
            assert 'q' in string

    def test_hangman_returns_a_string_with_the_same_length_as_the_word_to_guess_when_hard(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("HARD").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter c)
        string = Hangman().revealCorrectLetters(word, 'c')
        
        assert len(string) == len(word)

    def test_hangman_returns_a_string_with_hyphens_if_the_word_is_hard(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("HARD").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter d)
        string = Hangman().revealCorrectLetters(word, 'd')
        
        if '-' in word:
            assert '-' in string
        else:
            assert '-' not in string

    def test_hangman_raises_an_error_if_more_than_one_letter_guessed(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord().generateRandomWord(letter)
        self.assertRaises(ValueError, Hangman().revealCorrectLetters(word, letter * 2))

    def test_hangman_raises_an_error_if_empty_string_guessed(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord().generateRandomWord(letter)
        self.assertRaises(ValueError, Hangman().revealCorrectLetters(word, ""))

    def test_hangman_raises_an_error_if_empty_space_guessed(self) -> bool:
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord().generateRandomWord(letter)
        self.assertRaises(ValueError, Hangman().revealCorrectLetters(word, " "))
