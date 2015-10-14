import pygame
from buffalo import utils
from recipeManager import RecipeManager
from item import Item

class CraftingUI:

    BUTTON_SIZE = 32
    PADDING = 6

    def __init__(self, inventory):
        self.surface  = utils.empty_surface((228,500))
        self.surface.fill((100,100,100,100))
        self.pos = (utils.SCREEN_W / 2 - self.surface.get_width() / 2 - 350, utils.SCREEN_H / 2 - 150)
        self.updateRecipeTable()

    def updateRecipeTable(self):
        recipeTiles = list()
        total_y = 0
        RecipeManager.loadRecipes()
        for r in RecipeManager.RECIPES:
            newTile = self.generateRecipeTile(r)
            recipeTiles.append(newTile)
            total_y += newTile.get_height()
        newSurface = utils.empty_surface((228, total_y))
        newSurface.fill((100,100,100,100))
        currY = 0
        for surf in recipeTiles:
            newSurface.blit(surf, (0, currY))
            currY += surf.get_height()
        self.surface = newSurface


    def generateRecipeTile(self, recipe):
        y_length = 36 * (len(recipe.components.keys()) / 3) + 78;
        newScreen = utils.empty_surface((228, y_length))
        """
        Components Rendering
        """
        for num, item in enumerate(recipe.components.keys()):
            x = ((num % 3) * CraftingUI.BUTTON_SIZE) + CraftingUI.PADDING
            y = (((num / 3)) * CraftingUI.BUTTON_SIZE) + CraftingUI.PADDING
            newScreen.blit(Item(item).surface, (x,y))
        """
        Products Rendering
        """
        for item in recipe.products.keys():
            pass
        """
        Label Rendering
        """
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(str(recipe.name), 1, (255,255,0))
        newScreen.blit(label, (newScreen.get_width() - label.get_width() - 2, newScreen.get_height() - label.get_height() - 2))

        pygame.draw.rect(newScreen, (0,0,0,255), pygame.Rect(0,0,228, y_length), 1)
        return newScreen

    def blit(self, dest, pos):
        dest.blit(self.surface, pos)

    def update(self):
        pass

    def mouseDown(self, pos):
        pass