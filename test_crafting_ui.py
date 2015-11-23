from buffalo import utils
from craftingUI import CraftingUI
from inventory import Inventory
from recipe import Recipe
from recipeManager import RecipeManager

utils.init()

def test_init():
	i = Inventory()
	c = CraftingUI(i)
	assert c.inventory == i
	assert len(c.tileRects) == len(RecipeManager.RECIPES)
	assert len(c.tileRecipes) == len(RecipeManager.RECIPES)

def test_fail_recipe():
	pass

def test_success_recipe():
	pass