from enum import Enum
class Biome(Enum):
    #Tile Outputs
    ocean = 'o'
    forest = 'f'
    desert = 'd'
    grassland = 'g'
    mountain = 'm'
    peak = 'p'
    tundra = 't'
    tropical = 'r'
    shore = 's'

    #Height Constants
    ocean_height = 120
    shore_height = 125
    peak_height = 195
    mountain_height = 185

    #Moisture Constarints
    tundra_moisture = 180
    tropical_moisture = 145
    forest_moisture = 130
    grassland_moisture = 100
    desert_moisture = 0

    #Default Colors
    ocean_color = 0xFF0000
    forest_color = 0x005C09
    desert_color = (255,229,167)
    grassland_color = 0x018E0E
    mountain_color = 0x5F5F57
    peak_color = 0xFFFFFF
    tundra_color = (204, 242, 255)
    tropical_color = 0x00765D
    shore_color = (255,209,110)
