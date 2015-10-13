import sys

import pygame
from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label

from chunk import Chunk
from camera import Camera
from mapManager import MapManager
from pluginManager import PluginManager
from inventoryUI import InventoryUI
from inventory import Inventory
from guiManager import GUIManager
from craftingUI import CraftingUI

from playerCharacter import PlayerCharacter

class GameTestScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.BACKGROUND_COLOR = (0, 0, 0, 255)
        PluginManager.loadPlugins()
        Camera.init()
        self.pc = PlayerCharacter(
            Inventory(),
            name="Tom",
            fPos=(float(utils.SCREEN_M[0]), float(utils.SCREEN_M[1])),
            size=(32, 64),
        )
        Camera.lock(self.pc)
        self.UIManager = GUIManager()
        self.UIManager.guiScreens.append(InventoryUI(self.pc.inventory, self.UIManager))
        self.UIManager.guiScreens.append(CraftingUI(self.pc.inventory))
        self.UIManager.updateGUIs()


    def on_escape(self):
        sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        self.pc.update(keys)
        self.UIManager.update()
        Camera.update()

    def blit(self):
        Camera.blitView()
        self.UIManager.blit(utils.screen, (0,0))
        self.pc.blit(utils.screen)
