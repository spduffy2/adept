import sys

import pygame

from buffalo import utils
from buffalo.scene import Scene

class EditMapTestScene(Scene):
    def on_escape(self):
        sys.exit()

    def blit(self):
        pass

    def update(self):
        pass

    def __init__(self):
        Scene.__init__(self)
