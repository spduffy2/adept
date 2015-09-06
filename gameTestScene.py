import pygame
from buffalo import utils
from buffalo.scene import Scene
from chunk import Chunk

class GameTestScene(Scene):
    def __init__(self):
        super().__init__()
        chunk = Chunk(0,0)
        exit()

    def on_escape(self):
        exit();
    def update(self):
        pass
    def blit(self):
        pass
