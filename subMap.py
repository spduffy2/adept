from serializable import Serializable
from mapManager import MapManager
from buffalo import utils

class SubMap:

    PATH = ["subMaps"]
    TILE_SIZE = 16

    def __init__(sizeX,sizeY,id,posX=0,posY=0):
        self.size = sizeX,sizeY
        self.pos = posX,posY
        self.tileMap = [[None for _x in range(self.sizeX)] for _y in range(self.sizeY)]
        self.fromFile()
        self.surface = utils.empty_surface((sizeX * SubMap.TILE_SIZE, sizeY * SubMap.TILE_SIZE))

    def toFile(self):
        LOAD_PATH = MapManager.BASE_PATH + [MapManager.activeMap.name, SubMap.PATH]
        url = os.path.join(*list(LOAD_PATH + [id + '.smap']))

        output = ""
        for y in range(len(self.size[1])):
            for x in range(len(self.size[0])):
                if self.tileMap[x][y] is not None:
                    output += self.tileMap[x][y].serialize() + "\n"

        with open(url,'w+') as subMapFile:
            subMapFile.write(output)

    def fromFile(self):
        LOAD_PATH = MapManager.BASE_PATH + [MapManager.activeMap.name, SubMap.PATH]
        url = os.path.join(*list(LOAD_PATH + [id + '.smap']))

        tiles = list()
        with open(url,'r') as subMapFile:
            for tileLine in subMapFile:
                tiles.append(Serializable.to_object(tileLine))

        for tile in tiles:
            self.tileMap[tile.pos[0]][tile.pos[1]] = tile

    def render(self):
        for y in range(len(self.size[1])):
            for x in range(len(self.size[0])):
                self.surface.blit(self.tileMap[x][y].surface, (SubMap.TILE_SIZE * x, SubMap.TILE_SIZE * y))

    def blit(self, dest, pos):
        dest.blit( self.surface, pos )

