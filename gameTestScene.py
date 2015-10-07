import sys

import pygame
from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label

from chunk import Chunk
from camera import Camera
from mapManager import MapManager
from pluginManager import PluginManager

from playerCharacter import PlayerCharacter

class GameTestScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.BACKGROUND_COLOR = (0, 0, 0, 255)
        PluginManager.loadPlugins()
        Camera.init()
        self.pc = PlayerCharacter(
            name="Tom",
            size=(32, 64),
        )
        Camera.lock(self.pc)
        MapManager.loadChunks(0,0)

    def on_escape(self):
        sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        self.pc.update(keys)
        Camera.update()

    def blit(self):
        Camera.blitView()
        self.pc.blit(utils.screen)
