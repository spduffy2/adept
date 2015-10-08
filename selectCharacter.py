import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button
from buffalo.option import Option

class SelectCharacter(Scene):

    def on_escape(self):
        """
        Go back to the main menu
        """
        self.go_to_main_menu()

    def update(self):
        pass

    def blit(self):
        pass
    
    def __init__(self):
        super().__init__()
        self.BACKGROUND_COLOR = (50, 0, 177, 255)
        self.options.add(
            Option(
                utils.SCREEN_M,
                ["Character 1", "Character 2"],
                x_centered=True,
                y_centered=True,
            )
        )
        self.buttons.add(
            Button(
                (10, utils.SCREEN_H - 10),
                "Back",
                invert_y_pos=True,
                func=self.go_to_main_menu,
            )
        )

    def go_to_main_menu(self):
        utils.set_scene(
            Menu()
        )

from menu import Menu
