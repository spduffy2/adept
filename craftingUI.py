import pygame
from buffalo import utils

class craftingUI:

	BUTTON_SIZE = 32
	PADDING = 6

	def __init__(self, inventory, station_type):
		self.pos = (utils.SCREEN_W / 2 - self.surface.get_width() / 2, utils.SCREEN_H / 2 + 150)

	def updateRecipeTable(self):
		pass

	def generateRecipeTile(self):
		pass