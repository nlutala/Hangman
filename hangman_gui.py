'''
The GUI for the Hangman Game using the Arcade library

I used the following links to help with creating the screen:
- https://api.arcade.academy/en/latest/examples/gui_widgets.html#gui-widgets
- https://api.arcade.academy/en/latest/examples/gui_ok_messagebox.html#gui-ok-messagebox

Nathan Lutala
Github: https://github.com/nlutala
'''

import arcade
import arcade.gui
import random_letter
import random_hangman_word
import hangman

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Hangman"

class HangmanGUI(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.manager = None
        self.v_box = None
        self.letter = None
        self.word = None
        self.guesses = None
        self.hangman = None
        self.home_screen()

    def home_screen(self):
        '''
        Creates the starting screen for the Hangman game.
        '''
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        arcade.set_background_color(arcade.color.GRAY)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="Welcome to the Hangman Game",
                                              width=580,
                                              height=40,
                                              font_size=20,
                                              font_name="Kenney Future")
        self.v_box.add(ui_text_label.with_space_around(bottom=5))

        # Create the instructions, play game and quit buttons
        ui_flatbutton_instructions = arcade.gui.UIFlatButton(text="Instructions", width=200)
        self.v_box.add(ui_flatbutton_instructions.with_space_around(bottom=20))

        ui_flatbutton_play = arcade.gui.UIFlatButton(text="Play Game", width=200)
        self.v_box.add(ui_flatbutton_play.with_space_around(bottom=20))

        ui_flatbutton_quit = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(ui_flatbutton_quit.with_space_around(bottom=20))

        # Handle the clicks for the instructions, play game and quit buttons
        @ui_flatbutton_instructions.event("on_click")
        def on_click_flatbutton_instructions(event) -> None:
            self.on_click_instructions(event)

        @ui_flatbutton_play.event("on_click")
        def on_click_flatbutton_play(event) -> None:
            self.on_click_play_game(event)
        
        @ui_flatbutton_quit.event("on_click")
        def on_click_flatbutton_quit(event) -> SystemExit:
            arcade.exit()

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_instructions(self, event):
        '''
        Creates a new screen to display the instructions for the game.
        '''
        self.manager.clear()

        self.v_box = arcade.gui.UIBoxLayout()

        ui_text_label = arcade.gui.UITextArea(text="You need to guess the letters in a word that is randomly "
                                                    "generated. \n\n"
                                                    "After clicking the 'Play Game' button you will have the "
                                                    "option to "
                                                    "choose a level (Easy, Medium or Hard) and guess the letters"
                                                    " in the "
                                                    "word. \n\n"
                                                    "You will only be allowed to have a certain amount of wrong"
                                                    " guesses "
                                                    "before you lose the game. \n\n"
                                                    "If you make the correct guess before your number of "
                                                    "guesses run out, you win! \n\n"
                                                    "Are you ready to play?",
                                              width=480,
                                              height=300,
                                              font_size=15)
        self.v_box.add(ui_text_label.with_space_around(bottom=5))
        
        ui_flatbutton_back_to_start = arcade.gui.UIFlatButton(text="Back", width=200)
        self.v_box.add(ui_flatbutton_back_to_start.with_space_around(bottom=20))

        @ui_flatbutton_back_to_start.event("on_click")
        def ui_flatbutton_back_to_start(event) -> None:
            self.home_screen()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_play_game(self, event) -> None:
        '''
        Displays a new screen with a selection of different levels (easy, medium and hard)
        '''
        self.manager.clear()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="Pick your level",
                                              width=295,
                                              height=40,
                                              font_size=20,
                                              font_name="Kenney Future")
        self.v_box.add(ui_text_label.with_space_around(bottom=5))

        # Create the easy, medium and hard buttons
        ui_flatbutton_easy = arcade.gui.UIFlatButton(text="Easy", width=200)
        self.v_box.add(ui_flatbutton_easy.with_space_around(bottom=20))

        ui_flatbutton_medium = arcade.gui.UIFlatButton(text="Medium", width=200)
        self.v_box.add(ui_flatbutton_medium.with_space_around(bottom=20))

        ui_flatbutton_hard = arcade.gui.UIFlatButton(text="Hard", width=200)
        self.v_box.add(ui_flatbutton_hard.with_space_around(bottom=20))

        # Handle the clicks for the instructions, play game and quit buttons
        @ui_flatbutton_easy.event("on_click")
        def on_click_flatbutton_easy(event):
            self.letter = random_letter.RandomLetter().generateRandomLetter()
            self.word = random_hangman_word.RandomHangmanWord().generateRandomWord(self.letter)
            self.guesses = len(self.word) + 7
            self.hangman = hangman.Hangman()
            # Uncommment the print statement below to see the word in the console
            # print("Word for easy level:", self.word)
            self.on_click_play_easy(event, self.word)

        @ui_flatbutton_medium.event("on_click")
        def on_click_flatbutton_medium(event):
            self.letter = random_letter.RandomLetter().generateRandomLetter()
            self.word = random_hangman_word.RandomHangmanWord("MEDIUM").generateRandomWord(self.letter)
            self.guesses = len(self.word) + 5
            self.hangman = hangman.Hangman()
            # Uncommment the print statement below to see the word in the console
            # print("Word for medium level:", self.word)
            self.on_click_play_medium(event, self.word)
        
        @ui_flatbutton_hard.event("on_click")
        def on_click_flatbutton_hard(event):
            self.letter = random_letter.RandomLetter().generateRandomLetter()
            self.word = random_hangman_word.RandomHangmanWord("HARD").generateRandomWord(self.letter)
            self.guesses = len(self.word) + 3
            self.hangman = hangman.Hangman()
            # Uncommment the print statement below to see the word in the console
            # print("Word for hard level:", self.word)
            self.on_click_play_hard(event, self.word)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_play_easy(self, event, word_to_guess: str, revealed_letters="") -> None:
        '''
        The Hangman game at the easy level
        Here a player can play the Hangman game on easy mode
        '''
        self.manager.clear()
        # Uncommment the print statement below to see the word in the console
        # print(word_to_guess)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="Hangman: Easy",
                                              width=580,
                                              height=40,
                                              font_size=20,
                                              font_name="Kenney Future")
        self.v_box.add(ui_text_label.with_space_around(bottom=10))

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text=f"You have {self.guesses} guesses remaining",
                                              width=580,
                                              height=40,
                                              font_size=12,
                                              font_name="Kenney Future")
        self.v_box.add(ui_text_label.with_space_around(bottom=10))

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="Guess the word below",
                                              width=580,
                                              height=40,
                                              font_size=15,
                                              font_name="Kenney Future")
        self.v_box.add(ui_text_label.with_space_around(bottom=10))

        if len(revealed_letters) == 0:
            underscores = "_ " * len(self.word)
        else:
            underscores = " ".join(list(revealed_letters))

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text=underscores,
                                              width=580,
                                              height=40,
                                              font_size=15)
        self.v_box.add(ui_text_label.with_space_around(bottom=10))

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text=f"Incorrectly guessed letters: {self.hangman.getIncorrectGuesses()}",
                                              width=580,
                                              height=40,
                                              font_size=12)
        self.v_box.add(ui_text_label.with_space_around(bottom=15))

        if revealed_letters == word_to_guess:
            self.player_won_game(word_to_guess, event)  
        elif self.guesses == 0:
            self.player_lost_game(word_to_guess, event)
        else:
            # Create a text label
            ui_text_label = arcade.gui.UITextArea(text="Type a letter below and press submit",
                                                width=580,
                                                height=40,
                                                font_size=12,
                                                font_name="Kenney Future")
            self.v_box.add(ui_text_label.with_space_around(bottom=10))

            # Create a text area to add letters
            ui_input_text_label = arcade.gui.UIInputText()
            self.v_box.add(ui_input_text_label.with_space_around(bottom=10))

            # Add the submit button
            ui_flatbutton_submit = arcade.gui.UIFlatButton(text="Submit", width=200)
            self.v_box.add(ui_flatbutton_submit.with_space_around(bottom=20))            

            # Handle the click for the submit button so user input is received
            @ui_flatbutton_submit.event("on_click")
            def on_click_flatbutton_easy(event):
                revealed_letters = self.hangman.revealCorrectLetters(word_to_guess, ui_input_text_label.text)
                self.guesses -= 1
                self.on_click_play_easy(event, word_to_guess, revealed_letters)  

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_play_medium(self, event, word_to_guess: str, revealed_letters="") -> None:
        '''
        The Hangman game at the medium level
        Here a player can play the Hangman game on medium mode
        '''
        self.manager.clear()
        # Uncommment the print statement below to see the word in the console
        # print(word_to_guess)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="Hangman: Medium",
                                              width=580,
                                              height=40,
                                              font_size=20,
                                              font_name="Kenney Future")
        self.v_box.add(ui_text_label.with_space_around(bottom=10))

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text=f"You have {self.guesses} guesses remaining",
                                              width=580,
                                              height=40,
                                              font_size=12,
                                              font_name="Kenney Future")
        self.v_box.add(ui_text_label.with_space_around(bottom=10))

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="Guess the word below",
                                              width=580,
                                              height=40,
                                              font_size=15,
                                              font_name="Kenney Future")
        self.v_box.add(ui_text_label.with_space_around(bottom=10))

        if len(revealed_letters) == 0:
            underscores = "_ " * len(self.word)
        else:
            underscores = " ".join(list(revealed_letters))

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text=underscores,
                                              width=580,
                                              height=40,
                                              font_size=15)
        self.v_box.add(ui_text_label.with_space_around(bottom=10))

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text=f"Incorrectly guessed letters: {self.hangman.getIncorrectGuesses()}",
                                              width=580,
                                              height=40,
                                              font_size=12)
        self.v_box.add(ui_text_label.with_space_around(bottom=15))

        if revealed_letters == word_to_guess:
            self.player_won_game(word_to_guess, event)        
        elif self.guesses == 0:
            self.player_lost_game(word_to_guess, event)
        else:
            # Create a text label
            ui_text_label = arcade.gui.UITextArea(text="Type a letter below and press submit",
                                                width=580,
                                                height=40,
                                                font_size=12,
                                                font_name="Kenney Future")
            self.v_box.add(ui_text_label.with_space_around(bottom=10))

            # Create a text area to add letters
            ui_input_text_label = arcade.gui.UIInputText()
            self.v_box.add(ui_input_text_label.with_space_around(bottom=10))

            # Add the submit button
            ui_flatbutton_submit = arcade.gui.UIFlatButton(text="Submit", width=200)
            self.v_box.add(ui_flatbutton_submit.with_space_around(bottom=20))            

            # Handle the click for the submit button so user input is received
            @ui_flatbutton_submit.event("on_click")
            def on_click_flatbutton_easy(event):
                revealed_letters = self.hangman.revealCorrectLetters(word_to_guess, ui_input_text_label.text)
                self.guesses -= 1
                self.on_click_play_easy(event, word_to_guess, revealed_letters)  

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_play_hard(self, event, word_to_guess: str, revealed_letters="") -> None:
        '''
        The Hangman game at the hard level
        Here a player can play the Hangman game on hard mode
        '''
        self.manager.clear()
        # Uncommment the print statement below to see the word in the console
        # print(word_to_guess)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="Hangman: Medium",
                                              width=580,
                                              height=40,
                                              font_size=20,
                                              font_name="Kenney Future")
        self.v_box.add(ui_text_label.with_space_around(bottom=10))

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text=f"You have {self.guesses} guesses remaining",
                                              width=580,
                                              height=40,
                                              font_size=12,
                                              font_name="Kenney Future")
        self.v_box.add(ui_text_label.with_space_around(bottom=10))

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="Guess the word below",
                                              width=580,
                                              height=40,
                                              font_size=15,
                                              font_name="Kenney Future")
        self.v_box.add(ui_text_label.with_space_around(bottom=10))

        if len(revealed_letters) == 0:
            underscores = "_ " * len(self.word)
        else:
            underscores = " ".join(list(revealed_letters))

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text=underscores,
                                              width=580,
                                              height=40,
                                              font_size=15)
        self.v_box.add(ui_text_label.with_space_around(bottom=10))

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text=f"Incorrectly guessed letters: {self.hangman.getIncorrectGuesses()}",
                                              width=580,
                                              height=40,
                                              font_size=12)
        self.v_box.add(ui_text_label.with_space_around(bottom=15))

        if revealed_letters == word_to_guess:
            self.player_won_game(word_to_guess, event)      
        elif self.guesses == 0:
            self.player_lost_game(word_to_guess, event)
        else:
            # Create a text label
            ui_text_label = arcade.gui.UITextArea(text="Type a letter below and press submit",
                                                width=580,
                                                height=40,
                                                font_size=12,
                                                font_name="Kenney Future")
            self.v_box.add(ui_text_label.with_space_around(bottom=10))

            # Create a text area to add letters
            ui_input_text_label = arcade.gui.UIInputText()
            self.v_box.add(ui_input_text_label.with_space_around(bottom=10))

            # Add the submit button
            ui_flatbutton_submit = arcade.gui.UIFlatButton(text="Submit", width=200)
            self.v_box.add(ui_flatbutton_submit.with_space_around(bottom=20))            

            # Handle the click for the submit button so user input is received
            @ui_flatbutton_submit.event("on_click")
            def on_click_flatbutton_easy(event):
                revealed_letters = self.hangman.revealCorrectLetters(word_to_guess, ui_input_text_label.text)
                self.guesses -= 1
                self.on_click_play_easy(event, word_to_guess, revealed_letters)  

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def player_won_game(self, word_to_guess: str, event) -> None:
        '''
        Defines the creation of the screen shown if the player wins the game (at any level)
        '''
        self.manager.clear()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        ui_text_label = arcade.gui.UITextArea(text="You have correctly guessed the "
                                                    "word: \n\n"
                                                    f"{word_to_guess} \n\n"
                                                    f"With {self.guesses} guess(es) "
                                                    "remaning! \n\n"
                                                    "Well done! :) \n\n",
                                              width=390,
                                              height=200,
                                              font_size=15)
        self.v_box.add(ui_text_label.with_space_around(bottom=5))   

        # Add the play again button
        ui_flatbutton_play_again = arcade.gui.UIFlatButton(text="Play again", width=200)
        self.v_box.add(ui_flatbutton_play_again.with_space_around(bottom=20))

        # Handle the click for the play again button
        @ui_flatbutton_play_again.event("on_click")
        def on_click_flatbutton_play_again(event):
            self.on_click_play_game(event)

        # Add the quit button
        ui_flatbutton_quit = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(ui_flatbutton_quit.with_space_around(bottom=20))

        # Handle the click for the play again button
        @ui_flatbutton_quit.event("on_click")
        def on_click_flatbutton_quit(event):
            arcade.exit()

    def player_lost_game(self, word_to_guess: str, event) -> None:
        '''
        Defines the creation of the screen shown if the player loses the game (at any level)
        '''
        self.manager.clear()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        ui_text_label = arcade.gui.UITextArea(text="Unlucky! The word was: \n\n"
                                                    f"{word_to_guess} \n\n"
                                                    "You were unable to correctly "
                                                    "guess the word this time :( ",
                                              width=390,
                                              height=200,
                                              font_size=15)
        self.v_box.add(ui_text_label.with_space_around(bottom=5))   

        # Add the play again button
        ui_flatbutton_play_again = arcade.gui.UIFlatButton(text="Play again", width=200)
        self.v_box.add(ui_flatbutton_play_again.with_space_around(bottom=20))

        # Handle the click for the play again button
        @ui_flatbutton_play_again.event("on_click")
        def on_click_flatbutton_play_again(event):
            self.on_click_play_game(event)

        # Add the quit button
        ui_flatbutton_quit = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(ui_flatbutton_quit.with_space_around(bottom=20))

        # Handle the click for the play again button
        @ui_flatbutton_quit.event("on_click")
        def on_click_flatbutton_quit(event):
            arcade.exit()      
    
    # Not too sure what this does, but it's needed to display the GUI
    def on_draw(self) -> None:
        self.clear()
        self.manager.draw()


window = HangmanGUI()
arcade.run()
