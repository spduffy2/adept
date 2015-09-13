import sys
import random
from noise import snoise3
from PIL import Image
from biome import Biome

"""
Class that generates tile data for the world map with a given seed.
The generation algorithm uses Perlin noise to generate maps for both altitude and moisture.
(This requires the 'noise' library)
Based on the generated noise, biomes are determined.

The algorithm is (and must be) deterministic for any discrete seed, as the whole
game world will not be generated in a single call of the GenerateMap() function.
Rather, chunks may be requested from the generator using the map's seed, and the
location / size of the requested chunks.
"""

class MapGenerator:

    @staticmethod
    def GenerateMap(seed, startx, starty, sizex, sizey):
        #Constants needed for the perlin noise algorithm
        octaves = 8;
        freq = 64.0 * octaves
        """
        NOTE: Changing the value of freq essentially changes the scale / level
        of detail produced in the noise maps.
        """

        #Generate map seed if none was given
        if seed == None:
            seed = random.random()

        #Generate 2d Lists for height and moisture data
        heightMap = [[None]*sizex for _ in range(sizey)]
        moistureMap = [[None]*sizex for _ in range(sizey)]

        for outputy, y in enumerate(range(starty, sizey + starty)):
            for outputx, x in enumerate(range(startx, sizex + startx)):
                #Generate Perlin noise for the given x,y using the map seed as the z value
                #Map the noise to between 0 and 255
                heightMap[outputx][outputy] = int(snoise3(x / freq, y / freq, seed, octaves) * 127.0 + 128.0)
                #Change the z value so that moisture is determined by a different (but predictable) seed
                moistureMap[outputx][outputy] = int(snoise3(x / freq, y / freq, seed*100, octaves) * 127.0 + 128.0)
        MapGenerator.DrawMap(heightMap,moistureMap,sizex,sizey)

    def AssignBiomes(altitude,moisture,sizex,sizey):
        biomeMap = [[None]*sizex for _ in range(sizey)]
        for y in range(sizex):
            for x in range(sizey):
                #Mountain Peak
                if(altitude[x][y] > 195):
                    pixels[x,y] = (255,255,255)
                #Mountain
                elif(altitude[x][y]  > 185):
                    pixels[x,y] = 0x5F5F57
                #Forest
                elif(altitude[x][y]  > 155):
                    pixels[x,y] = 0x005C09
                #Grassland
                elif(altitude[x][y]  > 130):
                    pixels[x,y] = 0x018E0E
                #Sand
                elif(altitude[x][y]  > 120):
                    pixels[x,y] = (237,201,175)
                #Debug Chunk Markings
                if(x % 64 == 0 or y % 64 == 0):
                    pixels[x,y] = (50,50,50)

    @staticmethod
    def SmoothMoistureMap(moisture):
        pass

    @staticmethod
    def DrawMap(altitude,moisture,sizex,sizey):
        print Biome.forest

        #initializes new image
        img = Image.new("RGB", (sizex,sizey), "blue")
        pixels = img.load()
        #Iterate through all pixels
        for y in range(sizex):
            for x in range(sizey):
                #Mountain Peak
                if(altitude[x][y] > 195):
                    pixels[x,y] = (255,255,255)
                #Mountain
                elif(altitude[x][y]  > 185):
                    pixels[x,y] = 0x5F5F57
                #Forest
                elif(altitude[x][y]  > 155):
                    pixels[x,y] = 0x005C09
                #Grassland
                elif(altitude[x][y]  > 130):
                    pixels[x,y] = 0x018E0E
                #Sand
                elif(altitude[x][y]  > 120):
                    pixels[x,y] = (237,201,175)
                #Debug Chunk Markings
                if(x % 64 == 0 or y % 64 == 0):
                    pixels[x,y] = (50,50,50)

        img.show()
MapGenerator.GenerateMap(random.random(),1,1,512,512)
