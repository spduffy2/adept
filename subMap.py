from serializable import Serializable
from mapManager import MapManager

class SubMap:

    PATH = ["subMaps"]

    def __init__(sizeX,sizeY,id,posX=0,posY=0):
        self.size = sizeX,sizeY
        self.pos = posX,posY
        self.tileMap = [[None for _x in range(self.sizeX)] for _y in range(self.sizeY)]
        self.fromFile()

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
        tiles = list()
        input = "" #READ FILE
        for tileString in input.split():
            tiles.append(Serializable.to_object(tileString))

        for tile in tiles:
            self.tileMap[tile.pos[0]][tile.pos[1]] = tile
