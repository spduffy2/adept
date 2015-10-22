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

    #Best practice to make sure there aren't duplicate tile objects at same point in tileMap
    def addTile(self, tile):
        self.removeTileAtLoc(tile.pos)
        self.tileMap.append(tile)

    def getTileAtPos(self,pos):
        for tile in self.tileMap:
            if tile.pos[0] == pos[0] and tile.pos[1] == pos[1] and tile.pos[2] == pos[2]:
                return tile

    def removeTileAtLoc(self,pos):
        for tile in self.tileMap:
            if tile.pos[0] == pos[0] and tile.pos[1] == pos[1] and tile.pos[2] == pos[2]:
                self.tileMap.remove(tile)

    def render(self,player_loc=None):
        self.surface = utils.empty_surface((self.size[0] * SubMap.TILE_SIZE, self.size[1] * SubMap.TILE_SIZE))
        if player_loc is not None:
            print self.findAllNeighbors(self.tileMap[12])

        for tile in self.tileMap:
            if tile is not None:
                tile.render()
                self.surface.blit(tile.surface, (SubMap.TILE_SIZE * tile.pos[0], SubMap.TILE_SIZE * tile.pos[1]))

    def blit(self, dest, pos):
        dest.blit( self.surface, pos )

    def findAllNeighbors(self,tile):
        neighbors_found = 1
        neighbors = [tile]
        while neighbors_found is not 0:
            neighbors_found = 0
            for t in neighbors:
                immediateNeighbors = list()
                immediateNeighbors.append(self.getTileAtPos((t.pos[0]+1,t.pos[1],t.pos[2])))
                immediateNeighbors.append(self.getTileAtPos((t.pos[0]-1,t.pos[1],t.pos[2])))
                immediateNeighbors.append(self.getTileAtPos((t.pos[0],t.pos[1]+1,t.pos[2])))
                immediateNeighbors.append(self.getTileAtPos((t.pos[0],t.pos[1]-1,t.pos[2])))
                immediateNeighbors.append(self.getTileAtPos((t.pos[0],t.pos[1]-1,t.pos[2])))
                immediateNeighbors.append(self.getTileAtPos((t.pos[0],t.pos[1]-1,t.pos[2])))
                immediateNeighbors.append(self.getTileAtPos((t.pos[0],t.pos[1]-1,t.pos[2])))
                for n in immediateNeighbors:
                    if n is not None and n.buildingInternal is True and not n in neighbors:
                        neighbors.append(n)
                        neighbors_found += 1
        return neighbors

from tile import Tile