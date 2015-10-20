import math
import random

import pygame

from buffalo import utils

from npc import NPC

class Enemy(NPC):

	def __init__(self, name=None, fPos=None, **kwargs):
		NPC.__init__(self, name, fPos)

	def update(self, target):
		if self.fPos[0] != target.fPos[0] and math.hypot(self.fPos[1]-target.fPos[1], self.fPos[0]-target.fPos[0]) > 32 and math.hypot(self.fPos[1]-target.fPos[1], self.fPos[0]-target.fPos[0]) < 600:
			angle = math.atan((self.fPos[1]-target.fPos[1])/(self.fPos[0]-target.fPos[0]))
			if self.fPos[0] - target.fPos[0] > 0:
				angle = math.pi + angle
			self.move(angle)