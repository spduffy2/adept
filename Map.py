import os

from mapManager import MapManager

class Map:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.precedence = 0
        with open(os.path.join(*list(MapManager.BASE_PATH + [self.name, "properties.txt"]))) as mfile:
            for line in mfile:
                words = line.split()
                if len(words) >= 2:
                    if words[0] == "precedence":
                        try:
                            self.precedence = int(words[1])
                        except:  # If the second word can't be converted to an int
                            pass # Then don't do anything; keep precedence of 0
        self.loadChunks()

    def loadChunks(self):
        LOAD_PATH = MapManager.BASE_PATH + [self.name, "chunks"]
        files = [f for f in os.listdir(os.path.join(*LOAD_PATH)) if os.path.isfile(os.path.join(*list(LOAD_PATH + [f])))]
        self.chunk_files = [f for f in files if len(f) >= 9 and f[-6:] == ".chunk"]
