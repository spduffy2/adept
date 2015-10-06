import pygame
from buffalo import utils

class InventoryUI:
	def __init__(self,inventory):
		self.inventory = inventory
		self.padding = 5
		self.buttonSize = 35
		self.surface = utils.empty_surface((self.inventory.INV_SIZE_X * (self.buttonSize + self.padding) + self.padding,
			self.inventory.INV_SIZE_Y * (self.buttonSize + self.padding) + self.padding))
		self.surface.fill((0,0,0,100))
		self.pos = (utils.SCREEN_W / 2 - self.surface.get_width() / 2, utils.SCREEN_H / 2 - 150)
		self.pos = (0,0)

	def update(self):
		for x in range(0,self.inventory.INV_SIZE_X):
			for y in range(0,self.inventory.INV_SIZE_Y):
				iSurface = utils.empty_surface((35,35))
				#Default color
				iSurface.fill((100,100,100,255))

				#Load item icons from inventory
				if self.inventory.items[x][y]:
					iSurface = self.inventory.items[x][y].surface
				self.surface.blit(iSurface,((x * (self.buttonSize + self.padding)) + self.padding,
					(y * (self.buttonSize + self.padding) + self.padding)))

	def mouseDown(self,pos):
		self.pos = pos

	def blit(self, dest, pos):
		dest.blit(self.surface, pos)
