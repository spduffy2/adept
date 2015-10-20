import math
import random

import pygame

from buffalo import utils

from npc import NPC

class Friendly(NPC):

	def __init__(self, name=None, fPos=None, speed=None, **kwargs):
		speed = speed if speed is not None else .05
		NPC.__init__(self, name=name, fPos=fPos, speed = speed)
		self.currentDirection = random.random() * 2 * math.pi

	def update(self):
		self.currentDirection += random.random() * .5 - .25
		self.move(self.currentDirection)