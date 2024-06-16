'''
Test the functionality of the Hangman class
'''
import unittest
from hangman import Hangman
from random_hangman_word import RandomHangmanWord
from random_letter import RandomLetter

class TestHangman(unittest.TestCase):
    def test_hangman_returns_a_string_with_underscores_if_a_letter_is_not_in_the_word_when_easy(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("EASY").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter z)
        string = Hangman().revealCorrectLetters(word, 'z')
        
        if 'z' not in string:
            assert string == '_' * len(word)
        else:
            assert 'z' in string and "_" in string

    def test_hangman_returns_a_string_with_the_same_length_as_the_word_to_guess_when_easy(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("EASY").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter v)
        string = Hangman().revealCorrectLetters(word, 'v')
        
        assert len(string) == len(word)

    def test_hangman_returns_a_string_without_hyphens_if_the_word_is_easy(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("EASY").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter e)
        string = Hangman().revealCorrectLetters(word, 'e')
        
        assert '-' not in string

    def test_hangman_returns_a_string_with_underscores_if_a_letter_is_not_in_the_word_when_medium(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter x)
        string = Hangman().revealCorrectLetters(word, 'x')
        
        if 'x' not in string:
            assert string == '_' * len(word)
        else:
            assert 'x' in string and "_" in string

    def test_hangman_returns_a_string_with_the_same_length_as_the_word_to_guess_when_medium(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter b)
        string = Hangman().revealCorrectLetters(word, 'b')
        
        assert len(string) == len(word)

    def test_hangman_returns_a_string_without_hyphens_if_the_word_is_medium(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter g)
        string = Hangman().revealCorrectLetters(word, 'g')
        
        assert '-' not in string

    def test_hangman_returns_a_string_with_underscores_if_a_letter_is_not_in_the_word_when_hard(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("HARD").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter q)
        string = Hangman().revealCorrectLetters(word, 'q')
        
        if 'q' not in string:
            # What the string should be
            assertion_string = []
            for letter in word:
                if letter != "-":
                    assertion_string.append("_")
                else:
                    assertion_string.append(letter)
            assert string == "".join(assertion_string)
        else:
            assert 'q' in string and "_" in string

    def test_hangman_returns_a_string_with_the_same_length_as_the_word_to_guess_when_hard(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("HARD").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter c)
        string = Hangman().revealCorrectLetters(word, 'c')
        
        assert len(string) == len(word)

    def test_hangman_returns_a_string_with_hyphens_if_the_word_is_hard(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("HARD").generateRandomWord(letter)

        # I chose an arbitrary letter (in this case the letter d)
        string = Hangman().revealCorrectLetters(word, 'd')
        
        if '-' in word:
            assert '-' in string and "_" in string
        else:
            assert '-' not in string and "_" in string

    '''
    The following tests are now void as these will fail
    def test_hangman_raises_an_error_if_more_than_one_letter_guessed_when_easy(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("EASY").generateRandomWord(letter)
        with self.assertRaises(ValueError):
            Hangman().revealCorrectLetters(word, letter * 2)

    def test_hangman_raises_an_error_if_more_than_one_letter_guessed_when_medium(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)
        with self.assertRaises(ValueError):
            Hangman().revealCorrectLetters(word, letter * 2)

    def test_hangman_raises_an_error_if_more_than_one_letter_guessed_when_hard(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("HARD").generateRandomWord(letter)
        with self.assertRaises(ValueError):
            Hangman().revealCorrectLetters(word, letter * 2)
    '''

    def test_hangman_raises_an_error_if_empty_string_guessed(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord().generateRandomWord(letter)
        with self.assertRaises(ValueError):
            Hangman().revealCorrectLetters(word, "")

    def test_hangman_raises_an_error_if_empty_space_guessed(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord().generateRandomWord(letter)
        with self.assertRaises(ValueError):
            Hangman().revealCorrectLetters(word, " ")

    def test_hangman_raises_an_error_if_newline_guessed(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord().generateRandomWord(letter)
        with self.assertRaises(ValueError):
            Hangman().revealCorrectLetters(word, "\n")

    def test_getIncorrectGuesses_returns_only_distinct_letters(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)
        hangman = Hangman()
        hangman.revealCorrectLetters(word, "r")
        hangman.revealCorrectLetters(word, "r")

        if "r" not in word:
            assert hangman.getIncorrectGuesses().count("r") == 1
        else:
            assert hangman.getIncorrectGuesses().count("r") == 0

        # More manual test
        # Arbitrary word I chose myself
        word = "programming"

        hangman = Hangman()

        hangman.revealCorrectLetters(word, 'b')
        hangman.revealCorrectLetters(word, 'b')
        hangman.revealCorrectLetters(word, 'h')
        hangman.revealCorrectLetters(word, 'x')
        hangman.revealCorrectLetters(word, 'y')
        hangman.revealCorrectLetters(word, 'y')
        hangman.revealCorrectLetters(word, 'y')

        incorrect_guesses = hangman.getIncorrectGuesses().split(" ")

        for letter in incorrect_guesses:
            assert incorrect_guesses.count(letter) == 1

    def test___getIndexesOfALetterInAWord_returns_list_of_correct_occurences_of_a_letter_in_a_word_when_easy(self):
        # Arbitrary word I chose myself
        word1 = "programming"

        # Random letter RandomHangmanWord("HARD") generates
        letter = RandomLetter().generateRandomLetter()
        word2 = RandomHangmanWord("EASY").generateRandomWord(letter)

        hangman = Hangman()
        assert hangman._getIndexesOfALetterInAWord(word1, "m") == [6, 7]
        assert hangman._getIndexesOfALetterInAWord(word2, letter)[0] == 0

    def test___getIndexesOfALetterInAWord_returns_list_of_correct_occurences_of_a_letter_in_a_word_when_medium(self):
        # Arbitrary word I chose myself
        word1 = "programming"

        # Random letter RandomHangmanWord("HARD") generates
        letter = RandomLetter().generateRandomLetter()
        word2 = RandomHangmanWord("MEDIUM").generateRandomWord(letter)

        hangman = Hangman()
        assert hangman._getIndexesOfALetterInAWord(word1, "m") == [6, 7]
        assert hangman._getIndexesOfALetterInAWord(word2, letter)[0] == 0

    def test___getIndexesOfALetterInAWord_returns_list_of_correct_occurences_of_a_letter_in_a_word_when_hard(self):
        # Arbitrary word I chose myself
        word1 = "programming"

        # Random letter RandomHangmanWord("HARD") generates
        letter = RandomLetter().generateRandomLetter()
        word2 = RandomHangmanWord("HARD").generateRandomWord(letter)

        hangman = Hangman()
        assert hangman._getIndexesOfALetterInAWord(word1, "m") == [6, 7]
        assert hangman._getIndexesOfALetterInAWord(word2, letter)[0] == 0

    def test_revealCorrectLetters_returns_correct_word_if_it_stores_all_the_correct_letters(self):
        # Arbitrary word I chose myself
        word = "programming"

        hangman = Hangman()

        for letter in word:
            correct_letters = hangman.revealCorrectLetters(word, letter)

        assert word == correct_letters

    def test__checkInputIsLetter_returns_none_when_a_letter_is_correctly_inputted(self):
        letter = RandomLetter().generateRandomLetter()
        assert Hangman()._checkInputIsLetter(letter) == None

        letter = RandomLetter().generateRandomLetter()
        assert Hangman()._checkInputIsLetter(letter) == None

        letter = RandomLetter().generateRandomLetter()
        assert Hangman()._checkInputIsLetter(letter) == None

    def test_revealCorrectLetters_returns_word_to_guess_if_user_inputs_word(self):
        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("EASY").generateRandomWord(letter)
        assert Hangman().revealCorrectLetters(word, word) == word

        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("MEDIUM").generateRandomWord(letter)
        assert Hangman().revealCorrectLetters(word, word) == word

        letter = RandomLetter().generateRandomLetter()
        word = RandomHangmanWord("HARD").generateRandomWord(letter)
        assert Hangman().revealCorrectLetters(word, word) == word
