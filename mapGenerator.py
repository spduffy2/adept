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

    chunkSizeX = 64
    chunkSizeY = 64

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
                moistureMap[outputx][outputy] = int(snoise3(x / freq, y / freq, seed*10, octaves) * 127.0 + 128.0)
        biomeMap = MapGenerator.AssignBiomes(heightMap,moistureMap,sizex,sizey)
        return biomeMap

    @staticmethod
    def AssignBiomes(altitude,moisture,sizex,sizey):
        biomeMap = [[None]*sizex for _ in range(sizey)]
        for y in range(sizex):
            for x in range(sizey):
                #ocean
                if(altitude[x][y] <= Biome.ocean_height):
                    biomeMap[x][y] = Biome.ocean
                #shore
                elif(altitude[x][y] <= Biome.shore_height):
                    biomeMap[x][y] = Biome.shore
                #Mountain Peak
                elif(altitude[x][y] >= Biome.peak_height):
                    biomeMap[x][y] = Biome.peak
                #Mountain
                elif(altitude[x][y] >= Biome.mountain_height):
                    biomeMap[x][y] = Biome.mountain
                #tundra
                elif(moisture[x][y] >= Biome.tundra_moisture):
                    biomeMap[x][y] = Biome.tundra
                #tropical
                elif(moisture[x][y] >= Biome.tropical_moisture):
                    biomeMap[x][y] = Biome.tropical
                #Forest
                elif(moisture[x][y] >= Biome.forest_moisture):
                    biomeMap[x][y] = Biome.forest
                #Grassland
                elif(moisture[x][y] >= Biome.grassland_moisture):
                    biomeMap[x][y] = Biome.grassland
                #desert
                elif(moisture[x][y] >= Biome.desert_moisture):
                    biomeMap[x][y] = Biome.desert

        return biomeMap

    @staticmethod
    def SmoothMoistureMap(moisture):
        """
        TODO
        """
        pass

    @staticmethod
    def GenerateChunk(seed,chunkx, chunky):
        worldx = chunkx * 64
        worldy = chunky * 64
        return MapGenerator.GenerateMap(seed, worldx, worldy, MapGenerator.chunkSizeX, MapGenerator.chunkSizeY)

    @staticmethod
    def DrawMap(biomeMap):
        #initializes new image
        img = Image.new("RGB", (len(biomeMap),len(biomeMap[0])), "blue")
        pixels = img.load()
        #Iterate through all pixels
        for y in range(len(biomeMap)):
            for x in range(len(biomeMap[0])):
                #Mountain Peak
                if(biomeMap[x][y] == Biome.peak):
                    pixels[x,y] = Biome.peak_color
                #Mountain
                elif(biomeMap[x][y] == Biome.mountain):
                    pixels[x,y] = Biome.mountain_color
                #Forest
                elif(biomeMap[x][y] == Biome.forest):
                    pixels[x,y] = Biome.forest_color
                #Grassland
                elif(biomeMap[x][y] == Biome.grassland):
                    pixels[x,y] = Biome.grassland_color
                #desert
                elif(biomeMap[x][y] == Biome.desert):
                    pixels[x,y] = Biome.desert_color
                #ocean
                elif(biomeMap[x][y] == Biome.ocean):
                    pixels[x,y] = Biome.ocean_color
                #shore
                elif(biomeMap[x][y] == Biome.shore):
                    pixels[x,y] = Biome.shore_color
                #tropical
                elif(biomeMap[x][y] == Biome.tropical):
                    pixels[x,y] = Biome.tropical_color
                #tundra
                elif(biomeMap[x][y] == Biome.tundra):
                    pixels[x,y] = Biome.tundra_color
                else:
                    pixels[x,y] = 0x000000
                    #Biome not assigned

        img.show()
#MapGenerator.GenerateMap(random.random(),0,0,16*MapGenerator.chunkSizeX,16*MapGenerator.chunkSizeY)
