import math

import pygame

from buffalo import utils

from camera import Camera
from character import Character

class NPC(Character):

	def __init__(self, name=None, fPos=None, size=None, level=None, **kwargs):
		self.level = level if level is not None else 0
		Character.__init__(self, name=name, fPos=fPos, size=size)
		self.speed = kwargs.get('speed') if kwargs.get('speed') is not None else .1
		self.color = kwargs.get('color') if kwargs.get('color') is not None else (0,0,0,255)
		self.surface = utils.empty_surface(self.size)
		self.surface.fill(self.color)
		self.pos = int(self.fPos[0]),int(self.fPos[1])

	def move(self, direction=0):
		x, y = self.fPos
		x += self.speed * math.cos(direction) * utils.delta
		y += self.speed * math.sin(direction) * utils.delta
		self.fPos = x, y
		self.pos = int(self.fPos[0]),int(self.fPos[1])

	def blit(self, dest):
		x, y = self.pos
		dest.blit(self.surface, (x - Camera.pos[0], y - Camera.pos[1]))