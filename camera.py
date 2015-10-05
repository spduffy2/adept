import pygame

from buffalo import utils

from chunk import Chunk
from mapManager import MapManager

class Camera:
    """
    Manages what is drawn on the screen
    and how it is drawn
    """

    zoom = 1.0
    pos  = 0, 0
    fPos = 0.0, 0.0
    locked = False

    @staticmethod
    def init():
        """
        TODO: Fix mapManager / Camera link so that chunks are dynamically loaded
        """
        for row in range(MapManager.LC_HEIGHT):
            for col in range(MapManager.LC_WIDTH):
                x, y = col - MapManager.LC_WIDTH // 2, row - MapManager.LC_HEIGHT // 2
                MapManager.loadedChunks[row][col] = Chunk(x, y)

    @staticmethod
    def lock(character):
        """
        Lock the camera to a Character
        """
        Camera.locked = True
        Camera.character = character

    @staticmethod
    def update():
        if Camera.locked:
            x, y = Camera.character.fPos
            x, y = x - utils.SCREEN_W // 2, y - utils.SCREEN_H // 2
            Camera.updatePos((x, y))

    @staticmethod
    def updatePos(fPos):
        """
        The argument passed MUST be a tuple of two floating-point values
        """
        Camera.fPos = fPos
        Camera.pos = int(Camera.fPos[0]), int(Camera.fPos[1])
        # if fPos is somewhere where must load chunks
        # then load the chunks

    @staticmethod
    def blitView():
        rmult = Chunk.TILE_SIZE * Chunk.CHUNK_HEIGHT
        cmult = Chunk.TILE_SIZE * Chunk.CHUNK_WIDTH
        for rowindx, row in enumerate(MapManager.loadedChunks):
            for colindx, chunk in enumerate(row):
                x = colindx - MapManager.LC_WIDTH // 2
                y = rowindx - MapManager.LC_HEIGHT // 2
                chunk.blit(
                    utils.screen,
                    (cmult * x - Camera.pos[0], rmult * y - Camera.pos[1])
                )
