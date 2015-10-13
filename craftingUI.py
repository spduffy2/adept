import pygame
from buffalo import utils
from recipeManager import RecipeManager

class CraftingUI:

	BUTTON_SIZE = 32
	PADDING = 6

	def __init__(self, inventory):
		self.surface  = utils.empty_surface((228,500))
		self.surface.fill((100,100,100,100))
		self.pos = (utils.SCREEN_W / 2 - self.surface.get_width() / 2 - 350, utils.SCREEN_H / 2 - 150)

	def updateRecipeTable(self):
		recipeTiles = list()
		total_y = 0
		for r in RecipeManager.RECIPES:
			newTile = generateRecipeTile(r)
			recipeTiles.append(newTile)
			total_y += newTile.get_height()


	def generateRecipeTile(self, recipe):
		y_length = 36 * (len(recipe.components.keys) / 3) + 78;
		newScreen = utils.empty_surface((228, y_length))
		for item in recipe.components.keys:
			pass
		for item in recipe.products.keys:
			pass
		return newScreen

	def blit(self, dest, pos):
		dest.blit(self.surface, pos)

	def update(self):
		pass

	def mouseDown(self, pos):
		pass