import sys
import random
from noise import snoise3
from PIL import Image

# import time
# start_time = time.time()

class MapGenerator:

    @staticmethod
    def GenerateMap(seed, startx, starty, sizex, sizey):
        octaves = 8;
        freq = 64.0 * octaves
        #Generate map seed if none was given
        if seed == None:
            seed = random.random()

        heightMap = [[None]*sizex for _ in range(sizey)]

        moistureMap = [[None]*sizex for _ in range(sizey)]

        for outputy, y in enumerate(range(starty, sizey + starty)):
            for outputx, x in enumerate(range(startx, sizex + startx)):
                #Generate Perlin noise for the given x,y using the map seed as the z value
                #Map the noise to between 0 and 255
                heightMap[outputx][outputy] = int(snoise3(x / freq, y / freq, seed, octaves) * 127.0 + 128.0)
                #print "("+str(x)+","+str(y)+") " + str(heightMap[x][y])
                moistureMap[outputx][outputy] = int(snoise3(x / freq, y / freq, seed*100, octaves) * 127.0 + 128.0)

        MapGenerator.DrawMap(heightMap,moistureMap,sizex,sizey)



    @staticmethod
    def SmoothMoistureMap(moisture):
        pass

    @staticmethod
    def DrawMap(altitude,moisture,sizex,sizey):
        img = Image.new("RGB", (sizex,sizey), "blue")
        pixels = img.load()
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
                    #Chunk Markings
                if(x % 64 == 0 or y % 64 == 0):
                    pixels[x,y] = (50,50,50)
                #f.write(str(heightMap[x][y]) + "\n")
                #print "("+str(x)+","+str(y)+") " + str(altitude[x][y])
        img.show()
MapGenerator.GenerateMap(1,1,1,512,512)
