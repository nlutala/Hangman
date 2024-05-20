'''
The GUI for the Hangman Game using the Arcade library

I used the following links to help with creating the screen:
- https://api.arcade.academy/en/latest/examples/gui_widgets.html#gui-widgets
- https://api.arcade.academy/en/latest/examples/gui_ok_messagebox.html#gui-ok-messagebox
'''
# TODO #1: Refactor the method names to make this file easier to read and understand

import arcade
import arcade.gui

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Hangman"

class HangmanGUI(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.manager = None
        self.v_box = None
        
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

        # Handle the clicks for the play game and quit buttons
        @ui_flatbutton_instructions.event("on_click")
        def on_click_flatbutton_instructions(event):
            self.on_click_open(event)

        @ui_flatbutton_play.event("on_click")
        # TODO #2: Implement a screen where the user can select the level
        # of difficulty
        # TODO #3: Implement the Hangman game
        def on_click_flatbutton_play(event):
            print("Play Game button was pressed", event)
        
        @ui_flatbutton_quit.event("on_click")
        def on_click_flatbutton_quit(event):
            arcade.exit()

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_open(self, event):
        self.clear()
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
            callback=self.on_message_box_close,
            buttons=["Ok"]
        )

        self.manager.add(message_box)

    def on_click_start(self, event):
        print("Start:", event)

    def on_message_box_close(self, button_text):
        print(f"User pressed {button_text}.")

    def on_draw(self):
        self.clear()
        self.manager.draw()


window = HangmanGUI()
arcade.run()
