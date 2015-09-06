class Chunk:
    CHUNK_HEIGHT, CHUNK_WIDTH = 64,64
    def __init__(self, x, y):
        """
        Parsing definition
        """

        self.pos = x,y
        self.defs = dict()
        self.data = [["" for x in range(Chunk.CHUNK_WIDTH)] for y in range(Chunk.CHUNK_HEIGHT)]
        self.fromFile(x,y)

    def fromFile(self,x,y):
        """
        Need to account for different OS's for data folder
        """
        url = "chunks/" + str(x) + "," + str(y) + ".chunk"
        
        """
        Need to account for chunk not existing
        """
        with open(url,"r") as chunkFile:
            row = 0
            for line in chunkFile:
                if line.strip():
                    lineSplit = line.strip().split()
                    if line.strip().split()[0] == "define":
                        self.defs[lineSplit[1]] = int("0x"+lineSplit[3][1:3],16), int("0x"+lineSplit[3][3:5],16), int("0x"+lineSplit[3][5:7],16)
                        print(self.defs[line.strip().split()[1]])
                    else:
                        #data
                        for col, key in enumerate(lineSplit):
                            if col < Chunk.CHUNK_WIDTH and row < Chunk.CHUNK_HEIGHT:
                                self.data[row][col] = key
                        row += 1
