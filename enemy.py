import math
import random

import pygame

from buffalo import utils

from npc import NPC
from AStar import AStar

class Enemy(NPC):

	# Class for anything hostile. For now it just follows the player around,
	# There's not enough in the game in terms of health, damage, and item usage
	# To have actual combat

	def __init__(self, name=None, fPos=None, **kwargs):
		speed = kwargs.get("speed") if kwargs.get("speed") is not None else .05
		NPC.__init__(self, name=name, fPos=fPos, speed=speed, spawn=kwargs.get("spawn"))

	def update(self, target, submaps):
		# If it's close enough to the player it won't move
		# If it's too far away it will stop trying
		targetPos = target.fPos
		if self.fPos[0] != targetPos[0] and math.hypot(self.fPos[1]-targetPos[1], self.fPos[0]-targetPos[0]) > 32 and math.hypot(self.fPos[1]-targetPos[1], self.fPos[0]-targetPos[0]) < 600:
			
			newTargetPos = AStar.aStar(self.fPos, target.fPos, submaps)
			specialTargetPos = newTargetPos[1]
			targetPos = (specialTargetPos[0]*32, specialTargetPos[1]*32)
			print self.fPos
			print targetPos
			if targetPos is not None:
				angle = math.atan((self.fPos[1]-targetPos[1])/(self.fPos[0]-targetPos[0]))
				if self.fPos[0] - targetPos[0] > 0:
					angle = math.pi + angle
				self.move(submaps, angle)

		NPC.update(self)
