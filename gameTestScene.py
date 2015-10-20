import sys

import pygame
from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label

from saves import Saves
from chunk import Chunk
from camera import Camera
from mapManager import MapManager
from pluginManager import PluginManager
from inventoryUI import InventoryUI
from inventory import Inventory
from guiManager import GUIManager

from playerCharacter import PlayerCharacter
from friendly import Friendly
from enemy import Enemy

class GameTestScene(Scene):
    def __init__(self, pc=None):
        Scene.__init__(self)
        self.BACKGROUND_COLOR = (0, 0, 0, 255)
        PluginManager.loadPlugins()
        Camera.init()
        pc = Saves.unstore(pc, "characters")
        self.pc = pc if pc is not None else PlayerCharacter(
                Inventory(),
                name="Sean",
                size=(32, 64),
                speed=.25,
            )
        self.enemy = Enemy(name="monster", fPos=(0,0))
        self.friendly = Friendly(name="villager", fPos=(0,0))
        Camera.lock(self.pc)
        self.UIManager = GUIManager()
        self.UIManager.guiScreens.append(InventoryUI(self.pc.inventory, self.UIManager))
        self.UIManager.updateGUIs()

        MapManager.loadChunks(0,0)

    def on_escape(self):
        print(self.enemy.pos)
        print(self.friendly.pos)
        print(self.pc.pos)
        Saves.store(self.pc)
        sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        self.pc.update(keys)
        self.enemy.update(self.pc)
        self.friendly.update()
        self.UIManager.update()
        Camera.update()

    def blit(self):
        Camera.blitView()
        self.UIManager.blit(utils.screen, (0,0))
        self.pc.blit(utils.screen)
        self.enemy.blit(utils.screen)
        self.friendly.blit(utils.screen)
