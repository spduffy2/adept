import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button

class Menu(Scene):

    def __init__(self):
        super().__init__()
        self.labels.add(
            Label(
                (5, 5),
                "Adept 0.0 Alpha + 29 August 2015",
            )
        )

    def on_escape(self):
        exit()

    def update(self):
        pass

    def blit(self):
        pass
