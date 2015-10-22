from serializable import Serializable
from mapManager import MapManager
from buffalo import utils

import os

class SubMap:

    PATH = ["submaps"]
    TILE_SIZE = 32

    def __init__(self,sizeX,sizeY,_id,posX=0,posY=0,posZ=0):
        self.size = sizeX,sizeY
        self.id = _id
        self.pos = posX,posY,posZ
        self.tileMap = list()
        self.fromFile()
        self.surface = utils.empty_surface((self.size[0] * SubMap.TILE_SIZE, self.size[1] * SubMap.TILE_SIZE))
        self.render()

    def toFile(self):
        LOAD_PATH = MapManager.BASE_PATH + [MapManager.activeMap.name] + SubMap.PATH
        url = os.path.join(*list(LOAD_PATH + [str(self.id) + '.smap']))

        output = ""
        for tile in self.tileMap:
            if tile is not None:
                    output += tile.serialize() + "\n"

        with open(url,'w+') as subMapFile:
            subMapFile.write(output)

    def fromFile(self):
        LOAD_PATH = MapManager.BASE_PATH + [MapManager.activeMap.name] + SubMap.PATH
        url = os.path.join(*list(LOAD_PATH + [str(self.id) + '.smap']))
        if not os.path.isfile(url):
            print "Error: Tried to load SubMap with id \"" + str(self.id) + "\", but could not find the file."
            return

        with open(url,'r') as subMapFile:
            for tileLine in subMapFile:
                self.tileMap.append(Tile.deserialize(tileLine))

    def removeTileAtLoc(self,pos):
        for tile in self.tileMap:
            if tile.pos[0] == pos[0] and tile.pos[1] == pos[1]:
                self.tileMap.remove(tile)

    def render(self):
        for tile in self.tileMap:
            if tile is not None:
                tile.render()
                self.surface.blit(tile.surface, (SubMap.TILE_SIZE * tile.pos[0], SubMap.TILE_SIZE * tile.pos[1]))

    def blit(self, dest, pos):
        dest.blit( self.surface, pos )

from tile import Tile