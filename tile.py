from serializable import Serializable
from buffalo import utils
from subMap import SubMap
from mapManager import MapManager

import os
import pygame

class Tile(Serializable):
    def __init__(self,pos=(0,0),type_id=0,**kwargs):
        self.pos = pos
        self.type = type_id
        self.surface = utils.empty_surface((SubMap.TILE_SIZE,SubMap.TILE_SIZE))
        self.render()
        self.collisionEnabled = False

    def render(self):
        self.surface = utils.empty_surface((SubMap.TILE_SIZE,SubMap.TILE_SIZE))
        IMG_FILE = os.path.join(os.path.join(*list(MapManager.BASE_PATH + 
            [MapManager.activeMap.name] + SubMap.PATH + ['assets'] + [str(self.type) + ".png"])))
        try:
            self.surface = pygame.image.load(IMG_FILE)
        except Exception as e:
            print("Error: Icon for item \"" + str(self.type) + "\" does not exist.")
            print(e)
            IMG_FILE = os.path.join(os.path.join(*list(['tiles','assets'] + ["error.png"])))
            self.surface = pygame.image.load(IMG_FILE)

    def loadIDProperties(self):
        pass