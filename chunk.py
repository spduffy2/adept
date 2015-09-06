import os.path

"""
A Chunk is a data structure
that holds tiles.
"""
class Chunk:

    """
    CHUNK_HEIGHT and CHUNK_WIDTH represent
    the size, in tiles, of each Chunk
    """
    CHUNK_HEIGHT, CHUNK_WIDTH = 64,64

    def __init__(self, x, y):
        """
        This is the Chunk constructor.
        It creates a Chunk at the coordinates (<x>, <y>).
        <x> and <y> are positive or negative integers.
        
        self.pos  - a 2-tuple that stores the coordinates of the Chunk
        self.defs - a dictionary that stores definitions of tiles
                    self.defs' keys are specified in the file.
                    Each key maps to an RGBA 4-tuple, for now, at least.
        self.data - a two-dimensional array of strings
                    Each string is a key, which, when plugged into the
                    dictionary self.defs, returns an RGBA 4-tuple
        """

        self.pos = x,y
        self.defs = dict() 
        self.data = [["" for x in range(Chunk.CHUNK_WIDTH)] for y in range(Chunk.CHUNK_HEIGHT)]
        self.fromFile(x,y)

    def fromFile(self,x,y):
        """
        This method loads a chunk from a file.
        The chunk is specified by coordinates, <x> and <y>,
        which are positive or negative integers.
        """

        # Create a URL that's dependent on platform
        url = os.path.join("chunks", str(x) + "," + str(y) + ".chunk")

        # Be sure the URL points to a file before trying to open it
        if not os.path.isfile(url):
            print("Could not load chunk at URL '" + url + "'.")
            return

        with open(url,"r") as chunkFile:
            # Keep track of which row of data we want to fill
            row = 0
            
            for line in chunkFile:
                stripped = line.strip()
                # If the line isn't blank
                if stripped:
                    splitted = stripped.split()
                    if len(splitted) >= 4 and splitted[0] == "define": # If the definition is formatted correctly

                        # Then assign map the value to the specified key in self.defs
                        # This is an RGBA 4-tuple
                        self.defs[splitted[1]] = (
                            int("0x"+splitted[3][1:3],16), # R
                            int("0x"+splitted[3][3:5],16), # G
                            int("0x"+splitted[3][5:7],16), # B
                            255,                           # A = 255 = fully opaque
                        )
                        # This is RGBA and not RGB because Buffalo is written to handle transparency
                        # Pygame suffers huge performance losses when converting between RGB and RGBA
                        # surface types. If everything is RGBA then Pygame never has to convert surface
                        # types and thus does not suffer from these performance losses.

                    else: # If we aren't looking at a correctly formatted definition

                        # Then interprate the line as chunk data
                        for col, key in enumerate(splitted):
                            if col < Chunk.CHUNK_WIDTH and row < Chunk.CHUNK_HEIGHT:
                                self.data[row][col] = key

                        row += 1 # And remember to keep track of the row!
