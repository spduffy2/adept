from serializable import Serializable
from mapManager import MapManager
from buffalo import utils

import os

class SubMap:

    PATH = ["submaps"]
    TILE_SIZE = 16

    def __init__(self,sizeX,sizeY,_id,posX=0,posY=0):
        self.size = sizeX,sizeY
        self.id = _id
        self.pos = posX,posY
        self.tileMap = [[None for _x in range(self.size[0])] for _y in range(self.size[1])]
        self.fromFile()
        self.surface = utils.empty_surface((self.size[0] * SubMap.TILE_SIZE, self.size[1] * SubMap.TILE_SIZE))

    def toFile(self):
        LOAD_PATH = MapManager.BASE_PATH + [MapManager.activeMap.name] + SubMap.PATH
        url = os.path.join(*list(LOAD_PATH + [str(self.id) + '.smap']))

        output = ""
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if self.tileMap[x][y] is not None:
                    output += self.tileMap[x][y].serialize() + "\n"

        with open(url,'w+') as subMapFile:
            subMapFile.write(output)

    def fromFile(self):
        LOAD_PATH = MapManager.BASE_PATH + [MapManager.activeMap.name] + SubMap.PATH
        url = os.path.join(*list(LOAD_PATH + [str(self.id) + '.smap']))
        if not os.path.isfile(url):
            print "Error: Tried to load SubMap with id \"" + str(self.id) + "\", but could not find the file."
            return

        tiles = list()
        with open(url,'r') as subMapFile:
            for tileLine in subMapFile:
                tiles.append(Tile.deserialize(tileLine))

        for tile in tiles:
            tile.render()
            self.tileMap[tile.pos[0]][tile.pos[1]] = tile

    def render(self):
        for y in range(len(self.size[1])):
            for x in range(len(self.size[0])):
                self.surface.blit(self.tileMap[x][y].surface, (SubMap.TILE_SIZE * x, SubMap.TILE_SIZE * y))

    def blit(self, dest, pos):
        dest.blit( self.surface, pos )

from tile import Tile