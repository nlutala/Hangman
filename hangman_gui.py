'''
The GUI for the Hangman Game using the Arcade library

I used the following links to help with creating the screen:
- https://api.arcade.academy/en/latest/examples/gui_widgets.html#gui-widgets
- https://api.arcade.academy/en/latest/examples/gui_ok_messagebox.html#gui-ok-messagebox
'''

import arcade
import arcade.gui
import random_letter
import random_hangman_word

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
        self.guesses = 10 # Assuming there's 10 steps to drawing hangman
        
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
        # TODO: Implement the Hangman game
        def on_click_flatbutton_play(event) -> None:
            print("Play Game button was pressed", event)
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
        # The code in this function is run when we click the ok button.
        # The code below opens the message box and auto-dismisses it when done.
        message_box = arcade.gui.UIMessageBox(
            width=400,
            height=300,
            message_text=(
                "You need to guess the letters in a word that is randonly generated. \n\n"
                "After clicking the 'Play Game' button you will have the option to "
                "choose a level (Easy, Medium or Hard) and guess the letters in the "
                "word. \n\n"
                "You will only be allowed to have a certain amount of wrong guesses "
                "before you lose the game. \n\n"
                "If you make the correct guess before Hangman is drawn, you win! \n\n"
                "Are you ready to play?"
            ),
            callback=self.on_close_instructions,
            buttons=["Ok"]
        )

        self.manager.add(message_box)

    def on_close_instructions(self, button_text) -> None:
        print(f"User pressed {button_text}.")

    def on_click_play_game(self, event) -> None:
        self.manager.clear()

        # Create a vertical BoxGroup to align buttons
        self.v_box_play = arcade.gui.UIBoxLayout()

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="Pick your level",
                                              width=295,
                                              height=40,
                                              font_size=20,
                                              font_name="Kenney Future")
        self.v_box_play.add(ui_text_label.with_space_around(bottom=5))

        # Create the easy, medium and hard buttons
        ui_flatbutton_easy = arcade.gui.UIFlatButton(text="Easy", width=200)
        self.v_box_play.add(ui_flatbutton_easy.with_space_around(bottom=20))

        ui_flatbutton_medium = arcade.gui.UIFlatButton(text="Medium", width=200)
        self.v_box_play.add(ui_flatbutton_medium.with_space_around(bottom=20))

        ui_flatbutton_hard = arcade.gui.UIFlatButton(text="Hard", width=200)
        self.v_box_play.add(ui_flatbutton_hard.with_space_around(bottom=20))

        # Handle the clicks for the instructions, play game and quit buttons
        @ui_flatbutton_easy.event("on_click")
        def on_click_flatbutton_easy(event):
            self.letter = random_letter.RandomLetter().generateRandomLetter()
            self.word = random_hangman_word.RandomHangmanWord().generateRandomWord(self.letter)
            print("Word for easy level:", self.word)
            self.on_click_play_easy(event, self.word)

        @ui_flatbutton_medium.event("on_click")
        def on_click_flatbutton_medium(event):
            self.letter = random_letter.RandomLetter().generateRandomLetter()
            self.word = random_hangman_word.RandomHangmanWord("MEDIUM").generateRandomWord(self.letter)
            print("Word for medium level:", self.word)
            self.on_click_play_medium(event, self.word)
        
        @ui_flatbutton_hard.event("on_click")
        def on_click_flatbutton_hard(event):
            self.letter = random_letter.RandomLetter().generateRandomLetter()
            self.word = random_hangman_word.RandomHangmanWord("HARD").generateRandomWord(self.letter)
            print("Word for hard level:", self.word)
            self.on_click_play_hard(event, self.word)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box_play)
        )

    def on_click_play_easy(self, event, word_to_guess, revealed_letters="") -> None:
        self.manager.clear()
        print(word_to_guess)

        # Create a vertical BoxGroup to align buttons
        self.v_box_easy = arcade.gui.UIBoxLayout()

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="Hangman: Easy",
                                              width=580,
                                              height=40,
                                              font_size=20,
                                              font_name="Kenney Future")
        self.v_box_easy.add(ui_text_label.with_space_around(bottom=10))

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="Guess the word below",
                                              width=580,
                                              height=40,
                                              font_size=15,
                                              font_name="Kenney Future")
        self.v_box_easy.add(ui_text_label.with_space_around(bottom=10))

        # Will be delegated to another class which returns the new underscore sequence
        if len(revealed_letters) == 0:
            underscores = "_ " * len(self.word)
        else:
            underscores = " ".join(list(revealed_letters))

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text=underscores,
                                              width=580,
                                              height=40,
                                              font_size=15,
                                              font_name="Kenney Future")
        self.v_box_easy.add(ui_text_label.with_space_around(bottom=10))

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="Type a letter below and press submit",
                                              width=580,
                                              height=40,
                                              font_size=12,
                                              font_name="Kenney Future")
        self.v_box_easy.add(ui_text_label.with_space_around(bottom=10))

        # Create a text area to add letters
        ui_input_text_label = arcade.gui.UIInputText()
        self.v_box_easy.add(ui_input_text_label.with_space_around(bottom=10))

        # Add the submit button
        ui_flatbutton_submit = arcade.gui.UIFlatButton(text="Submit", width=200)
        self.v_box_easy.add(ui_flatbutton_submit.with_space_around(bottom=20))

        # Handle the clicks for the instructions, play game and quit buttons
        @ui_flatbutton_submit.event("on_click")
        def on_click_flatbutton_easy(event):
            # TODO
            self.on_click_play_easy(event, word_to_guess, ui_input_text_label.text)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box_easy)
        )

    def on_click_play_medium(self, event, word_to_guess) -> None:
        # self.manager.clear()
        pass

    def on_click_play_hard(self, event, word_to_guess) -> None:
        # self.manager.clear()
        pass
    
    # Not too sure what this does, but it's needed to display the GUI
    def on_draw(self) -> None:
        self.clear()
        self.manager.draw()


window = HangmanGUI()
arcade.run()
