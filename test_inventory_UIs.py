from inventoryUI import InventoryUI
from hotbarUI import HotbarUI
from buffalo import utils
from inventory import Inventory
from guiManager import GUIManager

utils.init()

def test_init_inventory():
	i = Inventory()
	g = GUIManager()
	ui = InventoryUI(i,g)
	assert ui.inventory
	assert ui.pos
	assert ui.itemRects is not None
	assert ui.guiManager
	assert ui.surface.get_size() == (ui.inventory.INV_SIZE_X * (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING) + InventoryUI.PADDING,
		ui.inventory.INV_SIZE_Y * (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING) + InventoryUI.PADDING)

def test_init_hotbar():
	i = Inventory()
	g = GUIManager()
	ui = HotbarUI(i,g)
	assert ui.inventory
	assert ui.pos
	assert ui.itemRects is not None
	assert ui.guiManager
	assert ui.selectedIndex == 0