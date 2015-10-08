import os, re

from mapManager import MapManager
import chunk

class Map:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.precedence = 0
        self.seed = 0
        path = os.path.join(os.path.join(*list(MapManager.BASE_PATH + [self.name, "properties.txt"])))
        if not os.path.isfile(path):
            print ("[Map] Error: No properties.txt found at \"" + path + "\". Creating an empty one.")
            if not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            with open(path, 'w+') as pfile:
                pass
        with open(os.path.join(*list(MapManager.BASE_PATH + [self.name, "properties.txt"]))) as mfile:
            for line in mfile:
                words = line.split()
                if len(words) >= 2:
                    if words[0] == "precedence":
                        try:
                            self.precedence = int(words[1])
                        except:  # If the second word can't be converted to an int
                            pass # Then don't do anything; keep precedence of 0
                    if words[0] == "seed":
                        try:
                            self.seed = float(words[1])
                        except:
                            pass
        self.loadChunks()

    def isChunkLoaded(self, x,y):
        for chunkFile in self.chunk_files:
            parsedName = re.split(r'\s+|[,.]\s*', chunkFile)
            if parsedName[0] == str(x) and parsedName [1] == str(y):
                return True
        return False

    def loadChunks(self):
        LOAD_PATH = MapManager.BASE_PATH + [self.name, "chunks"]
        if not os.path.exists(os.path.join(*LOAD_PATH)):
            print ("[Map] Error: No chunks folder found. Creating an empty one.")
            os.makedirs(os.path.join(*LOAD_PATH))
        files = [f for f in os.listdir(os.path.join(*LOAD_PATH)) if os.path.isfile(os.path.join(*list(LOAD_PATH + [f])))]
        self.chunk_files = [f for f in files if len(f) >= 9 and f[-6:] == ".chunk"]

    def loadChunk(self,chunkx, chunky):
        #Search loaded chunks to see if the desired chunk already exists
        for chunkFile in self.chunk_files:
            parsedName = re.split(r'\s+|[,.]\s*', chunkFile)
            if parsedName[0] == str(chunkx) and parsedName [1] == str(chunky):
                loadedChunk = chunk.Chunk(chunkx,chunky)
                loadedChunk.path = chunkFile
                loadedChunk.fromFile(chunkx,chunky)
                return loadedChunk
        #If the desired chunk does not exist, tell Chunk to create one
        genChunk = chunk.Chunk(chunkx, chunky)
        genChunk.generateDataAndDefs()
        genChunk.toFile()
        self.loadChunks()
        return chunk.Chunk(chunkx,chunky)
