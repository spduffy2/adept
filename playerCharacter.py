from buffalo import utils

from camera import Camera

from character import Character

class PlayerCharacter(Character):

    DEFAULT_NAME  = "Unnamed PlayerCharacter"
    DEFAULT_FPOS  = float(utils.SCREEN_M[0]), float(utils.SCREEN_M[1])
    DEFAULT_SIZE  = 32, 64
    DEFAULT_SPEED = 0.12

    def __init__(self, name=None, fPos=None, size=None, speed=None):
        name = name if name is not None else PlayerCharacter.DEFAULT_NAME
        fPos = fPos if fPos is not None else PlayerCharacter.DEFAULT_FPOS
        size = size if size is not None else PlayerCharacter.DEFAULT_SIZE
        Character.__init__(self, name=name, fPos=fPos, size=size)
        self.speed = speed if speed is not None else PlayerCharacter.DEFAULT_SPEED
        self.xv, self.yv = 0.0, 0.0
        self.surface = utils.empty_surface(self.size)
        self.surface.fill((170,170,170,255))

    def update(self):
        x, y = self.fPos
        x += self.xv * utils.delta
        y += self.yv * utils.delta
        self.fPos = x, y
        self.pos  = int(self.fPos[0]), int(self.fPos[1])
        self.xv, self.yv = 0, 0

    def blit(self, dest):
        x, y = self.pos
        cx, cy = Camera.pos
        dest.blit(self.surface, (x - cx, y - cy))
