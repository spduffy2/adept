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
from craftingUI import CraftingUI
from subMap import SubMap

from playerCharacter import PlayerCharacter

class GameTestScene(Scene):
    def __init__(self, pc_name):
        Scene.__init__(self)
        self.BACKGROUND_COLOR = (0, 0, 0, 255)
        PluginManager.loadPlugins()
        Camera.init()
        self.pc = Saves.unstore(pc_name, "characters")
        Camera.lock(self.pc)
        self.UIManager = GUIManager()
        self.UIManager.guiScreens.append(InventoryUI(self.pc.inventory, self.UIManager))
        self.UIManager.guiScreens.append(CraftingUI(self.pc.inventory))
        self.UIManager.updateGUIs()

        MapManager.loadChunks(0,0)

        s = SubMap(10,10,5)
        from tile import Tile 
        t = Tile((5,9,0),2,collisionEnabled=False)
        for x in range(10):
            for y in range(10):
                s.addTile(Tile(pos=(x,y,0),type_id=1,collisionEnabled=True))
        s.removeTileAtLoc((5,9,0))
        s.tileMap.append(t)
        s.toFile()
        MapManager.activeMap.submaps.append(s)

    def on_escape(self):
        Saves.store(self.pc)
        sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        subMaps = MapManager.activeMap.submaps
        self.pc.update(keys, subMaps)
        self.UIManager.update()
        Camera.update()

    def blit(self):
        Camera.blitView()
        self.UIManager.blit(utils.screen, (0,0))
        self.pc.blit(utils.screen)
