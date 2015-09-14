from enum import Enum
class Biome(Enum):
    #Tile Outputs
    ocean = 0
    forest = 1
    desert = 2
    grassland = 3
    mountain = 4
    peak = 5
    tundra = 6
    tropical = 7
    shore = 8

    #Height Constants
    ocean_height = 120
    shore_height = 125
    peak_height = 195
    mountain_height = 185

    #Moisture Constarints
    tropical_moisture = 180
    forest_moisture = 135
    grassland_moisture = 135
    desert_moisture = 125
    tundra_moisture = 0
