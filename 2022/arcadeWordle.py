import arcade
import os
from wordle import process_words, get_secret_word
import subprocess

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Wordle"
RADIUS = 150


# Classes
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
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the background window
        arcade.set_background_color(arcade.color.BLACK)

        # Set up the sprite lists
        self.max_guesses = 6
        self.cells = []
        self.create_cells()
        self.setup_cells()
        self.keys_by_char = {}
        self.create_keys()

        # game variables
        self.current_guess = ""
        self.current_guess_number = 0
        self.game_over = False
        self.secret_word = get_secret_word()
        self.jump_cells = arcade.SpriteList()
        self.show_word = False

    def play_line(self, n):
        text = ""
        if n == -1:
            r = range(self.max_guesses)
        else:
            r = range(n, n+1)
        for row in r:
            for sprite in self.cells[row]:
                text += sprite.char
            text += ". "
            for sprite in self.cells[row]:
                if sprite.texture_index == 1:
                    text += f"{sprite.char}. No. "
                elif sprite.texture_index == 2:
                    text += f"{sprite.char}. Move. "
                elif sprite.texture_index == 3:
                    text += f"{sprite.char}. Yes. "

        if text:
            self.say(text)

    def say(self, text):
        subprocess.Popen(['python3', 'playSound.py', text])

    def create_cells(self):
        for g in range(self.max_guesses):
            self.cells.append(arcade.SpriteList())

    def setup_cells(self):
        image_width = 56
        delta_x = image_width + 2
        delta_y = image_width + 2
        top_margin = 50
        center_x = int(SCREEN_WIDTH/2)

        top_left = Point(x=center_x - (delta_x * 2), y=SCREEN_HEIGHT - top_margin)
        current_location = top_left.clone()

        for g in range(self.max_guesses):
            current_location.x = top_left.x

            for c in range(5):
                cell = Cell(current_location)
                self.cells[g].append(cell)
                current_location.x += delta_x

            current_location.y -= delta_y

    def on_draw(self):
        # clear the screen
        self.clear()

        # draw each sprite list
        for r in range(self.max_guesses):
            self.cells[r].draw()

        self.keys.draw()
        if self.show_word:
            arcade.draw_text(self.secret_word,
                         SCREEN_WIDTH/2 - 40,
                         375,
                         arcade.color.WHITE,
                         18, bold=True)


    def on_update(self, delta_time: float):
        for cell in self.jump_cells:
            if cell.jump_state == 0:
                cell.jump_state = 1
                break
            if cell.jump_state == 1 or cell.jump_state == 2:
                break


        for r in range(self.max_guesses):
            self.cells[r].update()

        self.keys.update()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.P and modifiers & arcade.key.MOD_CTRL:
            self.play_line(-1)
            return
        if self.game_over:
            return

        if arcade.key.A <= symbol <= arcade.key.Z:
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            offset_of_symbol_from_a = symbol - arcade.key.A
            character = alphabet[offset_of_symbol_from_a]
            self.process_character(character)
        elif symbol == arcade.key.BACKSPACE:
            self.handle_backspace()
        elif symbol == arcade.key.RETURN or symbol == arcade.key.ENTER:
            self.handle_return()

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        keys = arcade.get_sprites_at_point((x, y), sprite_list=self.keys)
        if keys:
            key = keys[0]
            char = key.char
            if char == '⌫':
                self.handle_backspace()
            elif char == '⏎':
                self.handle_return()
            else:
                self.process_character(char)

    def shake(self):
        for cell in self.cells[self.current_guess_number]:
            cell.shake()

    def handle_return(self):

        if len(self.current_guess) != 5:
            self.shake()
            self.say("Too short.")
            return

        result = process_words(self.secret_word, self.current_guess)
        if result is None:
            self.shake()
            self.say("Invalid word.")
            return

        # update the cells
        for n, cell_type in enumerate(result):
            self.cells[self.current_guess_number][n].set_color(cell_type)
            self.keys_by_char[self.current_guess[n]].set_color(cell_type)

        if self.current_guess == self.secret_word:
            self.jump()
            self.say(f"{self.current_guess} is correct!")
            self.game_over = True
            return

        self.play_line(self.current_guess_number)
        self.current_guess_number += 1
        self.current_guess = ""

        if self.current_guess_number == self.max_guesses:
            self.show_word = True
            self.game_over = True
            self.say(f"Game over. The word was {self.secret_word}")

    def handle_backspace(self):
        guess_len = len(self.current_guess)
        if guess_len > 0:
            self.current_guess = self.current_guess[:-1]
            self.cells[self.current_guess_number][guess_len - 1].clear()

    def process_character(self, character):
        if len(self.current_guess) == 5:
            return
        self.current_guess += character
        guess_len = len(self.current_guess)
        cell_index = guess_len - 1
        self.cells[self.current_guess_number][cell_index].set_char(character)

    def create_keys(self):
        self.keys = arcade.SpriteList()
        key_width = 36
        key_height = 60
        start_x = 105
        delta_x = 8
        delta_y = 8

        location = Point(x=start_x, y=300)
        for char in "QWERTYUIOP":
            sprite = Key(char, location)
            self.keys_by_char[char] = sprite
            self.keys.append(sprite)
            location.x += key_width + delta_x

        location.x = start_x
        location.y -= (key_height + delta_y)
        location.x += key_width/2
        for char in "ASDFGHJKL":
            sprite = Key(char, location)
            self.keys_by_char[char] = sprite
            self.keys.append(sprite)
            location.x += key_width + delta_x

        location.x = start_x + key_width + delta_x + key_width/2
        location.y -= (key_height + delta_y)
        for char in "ZXCVBNM":
            sprite = Key(char, location)
            self.keys_by_char[char] = sprite
            self.keys.append(sprite)
            location.x += key_width + delta_x

        location.x += 9
        sprite = Key("⌫", location)
        self.keys.append(sprite)

        location.x = start_x + key_width - 27
        sprite = Key("⏎", location)
        self.keys.append(sprite)


    def jump(self):
        self.jump_cells = self.cells[self.current_guess_number]

class Cell(arcade.Sprite):
    def __init__(self, location):
        super().__init__()
        blank = os.path.join("images", "cells", "blank", "BLANK.png")
        self.append_texture(arcade.load_texture(blank))
        self.set_texture(0)
        self.texture_index = 0

        self.location = location.clone()
        self.center_x = self.location.x
        self.center_y = self.location.y
        self.is_moving = False
        self.direction_change = 0
        self.is_growing = False
        self.jump_state = 0
        self.success_animation_complete = False
        self.char = ''

    def set_char(self, char):
        gray = os.path.join("images", "cells", "gray", f"{char.upper()}.png")
        yellow = os.path.join("images", "cells", "yellow", f"{char.upper()}.png")
        green = os.path.join("images", "cells", "green", f"{char.upper()}.png")
        current = os.path.join("images", "cells", "current", f"{char.upper()}.png")

        self.textures = self.textures[:1]  # remove all but the first texture
        self.append_texture(arcade.load_texture(gray))
        self.append_texture(arcade.load_texture(yellow))
        self.append_texture(arcade.load_texture(green))
        self.append_texture(arcade.load_texture(current))
        self.texture_index = 4
        self.set_texture(4)
        self.is_growing = True
        self.scale = 0.2
        self.char = char

    def clear(self):
        self.set_texture(0)
        self.textures = self.textures[:1]

    def set_color(self, result_status):
        if result_status == 'current':
            self.texture_index = 4
        elif result_status == 'Y':
            self.texture_index = 3
        elif result_status == '-':
            self.texture_index = 2
        else:
            self.texture_index = 1
        self.set_texture(self.texture_index)

    def update(self):
        if self.is_moving:
            self.center_x += self.change_x
            self.direction_change += 1
            if self.change_x < 0:
                self.change_x = 10
            else:
                self.change_x = -10
            if self.direction_change == 4:
                self.is_moving = False
                self.center_x -= 5
                self.change_x = 0
                self.direction_change = 0
        if self.is_growing:
            self.scale = self.scale + 0.2
            if self.scale >= 1.6:
                self.is_growing = False
                self.scale = 1.0
        if self.jump_state == 1:
            self.center_y += 4
            if self.center_y >= self.location.y + 20:
                self.jump_state = 2
        if self.jump_state == 2:
            self.center_y -= 4
            if self.center_y <= self.location.y:
                self.jump_state = 3




    def shake(self):
        self.is_moving = True
        self.change_x = -5


class Key(arcade.Sprite):
    def __init__(self, char, location):
        super().__init__()
        self.center_x = location.x
        self.center_y = location.y
        self.char = char.upper()
        if char == "⌫":
            backspace = os.path.join("images", "keys", "backspace.png")
            self.textures.append(arcade.load_texture(backspace))
            self.set_texture(0)
            return
        elif char == "⏎":
            enter = os.path.join("images", "keys", "enter.png")
            self.textures.append(arcade.load_texture(enter))
            self.set_texture(0)
            return

        light_gray = os.path.join("images", "keys", "light_gray", f"{self.char}.png")
        gray = os.path.join("images", "keys", "gray", f"{self.char}.png")
        yellow = os.path.join("images", "keys", "yellow", f"{self.char}.png")
        green = os.path.join("images", "keys", "green", f"{self.char}.png")
        self.textures.append(arcade.load_texture(light_gray))
        self.textures.append(arcade.load_texture(gray))
        self.textures.append(arcade.load_texture(yellow))
        self.textures.append(arcade.load_texture(green))
        self.set_texture(0)
        self.current_texture_index = 0

    def set_color(self, result_status):
        if result_status == 'Y':
            texture_index = 3
        elif result_status == '-':
            texture_index = 2
        else:
            texture_index = 1

        if texture_index > self.current_texture_index:
            self.current_texture_index = texture_index
            self.set_texture(texture_index)



# Main code entry point
if __name__ == "__main__":
    app = Wordle()
    arcade.run()