import pygame
from buffalo import utils

class InventoryUI:

	BUTTON_SIZE = 35
	PADDING = 5

	def __init__(self,inventory, manager):
		self.inventory = inventory
		self.surface = utils.empty_surface((self.inventory.INV_SIZE_X * (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING) + InventoryUI.PADDING,
			self.inventory.INV_SIZE_Y * (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING) + InventoryUI.PADDING))
		self.surface.fill((0,0,0,100))
		self.pos = (utils.SCREEN_W / 2 - self.surface.get_width() / 2, utils.SCREEN_H / 2 - 150)
		self.itemRects = list()
		self.guiManager = manager

	def getGUIPosFromItemPos(self, pos):
		newX = pos[0] * (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING) + InventoryUI.PADDING
		newY = pos[1] * (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING) + InventoryUI.PADDING
		return (newX, newY)

	def getItemPosFromMousePos(self, pos):
		relPos = (pos[0] - self.pos[0], pos[1] - self.pos[1])
		itemX = (relPos[0] - InventoryUI.PADDING) / (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING)
		itemY = (relPos[1] - InventoryUI.PADDING) / (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING)
		return (itemX, itemY)

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

	def getItemFromGUIPos(self, pos):
		for x in range(0,self.inventory.INV_SIZE_X):
			for y in range(0,self.inventory.INV_SIZE_Y):
				if self.inventory.items[x][y] != None:
					itemRect = pygame.Rect(self.getGUIPosFromItemPos((x,y)), (InventoryUI.BUTTON_SIZE,InventoryUI.BUTTON_SIZE))
					if itemRect.collidepoint(pos):
						return self.inventory.items[x][y]
		return None

	def mouseDown(self,pos):
		if self.guiManager.draggedItem == None:
			item = self.getItemFromGUIPos(pos)
			self.inventory.removeItem(item)
			self.guiManager.draggedItem = item
		else:
			#Replaced by item at location, else None
			self.guiManager.draggedItem = self.inventory.placeItem(self.guiManager.draggedItem, self.getItemPosFromMousePos(pygame.mouse.get_pos()))
		self.update()


	def blit(self, dest, pos):
		dest.blit(self.surface, pos)
