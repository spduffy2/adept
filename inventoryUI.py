import pygame

class InventoryUI:
	def __init__(self,sizex,sizey,inventory):
		self.inventory = inventory
		self.surface = pygame.Surface((sizex,sizey))
		self.surface = pygame.Surface.fill((0,0,0))

	def blit(self, dest, pos):
		dest.blit(self.surface, pos)
