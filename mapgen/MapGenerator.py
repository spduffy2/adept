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
        img = Image.new("RGB", (sizex,sizey), "blue")
        pixels = img.load()
        xOutput = 0
        yOutput = 0
        for y in range(starty, sizey + starty):
            for x in range(startx, sizex + startx):
                #Generate Perlin noise for the given x,y using the map seed as the z value
                #Map the noise to between 0 and 256
                noise = int(snoise3(x / freq, y / freq, seed, octaves) * 127.0 + 128.0)
                if(noise > 195):
                    pixels[xOutput,yOutput] = (255,255,255)
                elif(noise > 185):
                    pixels[xOutput,yOutput] = 0x5F5F57
                elif(noise > 155):
                    pixels[xOutput,yOutput] = 0x005C09
                elif(noise > 130):
                    pixels[xOutput,yOutput] = 0x018E0E
                elif(noise > 120):
                    pixels[xOutput,yOutput] = (237,201,175)
                if(xOutput % 64 == 0 or yOutput % 64 == 0):
                    pixels[xOutput,yOutput] = (50,50,50)
                xOutput += 1
            xOutput = 0
            yOutput += 1

        img.show()
MapGenerator.GenerateMap(1,64,0,64,64)
