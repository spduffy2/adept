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
		self.itemRects = list()
	
	def getGUIPosFromItemPos(self, pos):
		newX = pos[0] * (self.buttonSize + self.padding) + self.padding
		newY = pos[1] * (self.buttonSize + self.padding) + self.padding
		return (newX, newY)

	def update(self):
		self.itemRects = dict()
		for x in range(0,self.inventory.INV_SIZE_X):
			for y in range(0,self.inventory.INV_SIZE_Y):
				iSurface = utils.empty_surface((35,35))
				#Default color
				iSurface.fill((100,100,100,255))

				#Load item icons from inventory
				if self.inventory.items[x][y]:
					iSurface = self.inventory.items[x][y].surface

				#Blit surface (default to empty surface)
				self.surface.blit(iSurface, self.getGUIPosFromItemPos((x,y)))

	def getItemFromPos(self, pos):
		for x in range(0,self.inventory.INV_SIZE_X):
			for y in range(0,self.inventory.INV_SIZE_Y):
				if self.inventory.items[x][y] != None:
					itemRect = pygame.Rect(self.getGUIPosFromItemPos((x,y)), (self.buttonSize,self.buttonSize))
					if itemRect.collidepoint(pos):
						return self.inventory.items[x][y]
		return None

		#Pixel-wise method:
		# newX = (pos[0] - self.padding) / (self.buttonSize + self.padding)
		# newY = (pos[1] - self.padding) / (self.buttonSize + self.padding)
		# return (newX, newY)

	def mouseDown(self,pos):
		item = self.getItemFromPos(pos)
		item.surface.fill((100,100,100,255))
		self.update()


	def blit(self, dest, pos):
		dest.blit(self.surface, pos)
