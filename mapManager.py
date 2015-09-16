import os

class MapManager:
    """
    Manages chunks and map loading
    """

    BASE_PATH          = ["maps"] # BASE_PATH is a list version of the base path in
                                  # which MapManager will search for chunks. For example,
                                  # if the base path should be maps/otherfolder/ then
                                  # BASE_PATH should equal ["maps", "otherfolder"]
    maps                = []      # Maps is a list of all Map's found in within BASE_PATH
    loadedChunks        = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
    LC_WIDTH, LC_HEIGHT = 3, 3    # LC_WIDTH and LC_HEIGHT are the maximum width and height
                                  # of loadedChunnks, which contains Chunk's loaded into memory

    @staticmethod
    def loadMap( map_name ):
        """
        loadMap takes one string map_name and attempts to load the corresponding map
        """
        LOAD_PATH = MapManager.BASE_PATH + [map_name, "chunks"]
        MapManager.maps.append(Map(map_name, LOAD_PATH))

    def loadMaps():
        """
        loadMaps loads all the maps that are checked in the plugins manager file
        """
        for name in PluginManager.mapNames:
            MapManager.loadMap(name)
        MapManager.maps.sort(key=lambda m: m.precedence)

from Map import Map
from pluginManager import PluginManager
