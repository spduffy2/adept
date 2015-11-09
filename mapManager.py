import os

class MapManager:
    """
    Manages chunks and map loading
    """

    BASE_PATH    = ["maps"] # BASE_PATH is a list version of the base path in
                            # which MapManager will search for chunks. For example,
                            # if the base path should be maps/otherfolder/ then
                            # BASE_PATH should equal ["maps", "otherfolder"]
    maps          = []      # Maps is a list of all Map's found in within BASE_PATH
    activeMap     = None    # activeMap is the active map // lol

    loaded_chunks = dict()

    @staticmethod
    def loadMaps():
        """
        loadMaps loads all the maps that are checked in the plugins manager file
        """
        for name in PluginManager.mapNames:
            MapManager.loadMap(name)
        MapManager.maps.sort(key=lambda m: m.precedence)
        MapManager.activeMap = MapManager.maps[0]

    @staticmethod
    def loadMap( map_name ):
        """
        loadMap takes one string map_name and attempts to load the corresponding map
        """
        CHUNK_PATH_LIST = MapManager.BASE_PATH + [map_name, "chunks"]
        MapManager.maps.append(Map(map_name, CHUNK_PATH_LIST))

    @staticmethod
    def get_chunk_coords(world_pos):
        return (
            int(world_pos[0] / (Chunk.CHUNK_WIDTH * Chunk.TILE_SIZE)),
            int(world_pos[1] / (Chunk.CHUNK_HEIGHT * Chunk.TILE_SIZE)),
        )

    @staticmethod
    def hard_load(world_pos):
        x, y = chunk_coords = MapManager.get_chunk_coords(world_pos)
        for j in range(y - 2, y + 3):
            for i in range(x - 2, x + 3):
                MapManager.loaded_chunks[(i, j)] = Chunk(i, j)
        

from Map import Map
from pluginManager import PluginManager
from chunk import Chunk
