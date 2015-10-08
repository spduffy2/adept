import pygame

from buffalo import utils

from camera import Camera
from character import Character

from inventory import Inventory
from skill import Skill

class PlayerCharacter(Character):

    DEFAULT_NAME  = "Unnamed PlayerCharacter"
    DEFAULT_FPOS  = float(utils.SCREEN_M[0]), float(utils.SCREEN_M[1])
    DEFAULT_SIZE  = 32, 64
    DEFAULT_SPEED = 0.02
    DEFAULT_COLOR = (170,170,170,255) #Added for testing purposes

    #**kwargs here allows for an object to be created with a dictionary for input, which basically allows an object to be created from the deserialize method
    def __init__(self, inventory, name=None, fPos=None, size=None, speed=None, **kwargs):
        name = name if name is not None else PlayerCharacter.DEFAULT_NAME #These could probably be rewritten with kwargs
        fPos = fPos if fPos is not None else PlayerCharacter.DEFAULT_FPOS
        size = size if size is not None else PlayerCharacter.DEFAULT_SIZE
        self.color = kwargs.get('color') if kwargs.get('color') is not None else PlayerCharacter.DEFAULT_COLOR #If there's a color given, it's color goes to that value, else it goes to default
        self.level = kwargs.get('level') if kwargs.get('level') is not None else 1
        self.experience = kwargs.get('experience') if kwargs.get('experience') is not None else 0
        Character.__init__(self, name=name, fPos=fPos, size=size)
        self.speed = speed if speed is not None else PlayerCharacter.DEFAULT_SPEED
        self.hide = Skill()
        self.skills = [hide]
        self.xv, self.yv = 0.0, 0.0
        self.surface = utils.empty_surface(self.size)
        self.inventory = inventory
        self.surface.fill(self.color)

    def update(self, keys):

        if keys[pygame.K_w]:
            self.yv += -self.speed
        if keys[pygame.K_s]:
            self.yv += self.speed
        if keys[pygame.K_d]:
            self.xv += self.speed
        if keys[pygame.K_a]:
            self.xv += -self.speed
        if keys[pygame.K_f]:
            self.skills[0].name(self)

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

    def gainXP(self, amount):
        self.experience += amount
        if self.experience >= 100*self.level:
            self.level += 1
            self.experience %= (100*self.level)