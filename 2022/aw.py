import arcade
from wordle import process_words, get_secret_word

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Wordle"

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)


class Wordle(arcade.Window):
    """Main welcome window
    """
    def __init__(self):
        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.BLACK)

        self.max_guesses = 6
        self.cells = []
        self.create_cells()
        self.setup_cells()
        # self.keys_by_char = {}
        # self.create_keys()

        # game variables
        self.current_guess = ""
        self.current_guess_number = 0
        self.game_over = False
        self.secret_word = get_secret_word()
        # self.jump_cells = arcade.SpriteList()
        self.show_word = False


    def create_cells(self):
        for g in range(self.max_guesses):
            self.cells.append(arcade.SpriteList())
