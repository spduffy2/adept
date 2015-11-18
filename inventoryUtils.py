from inventory import Inventory
from eventRegistry import EventRegistry
from playerConsole import PlayerConsole

class InventoryUtils:
	@staticmethod
	def init():
		EventRegistry.registerListener(InventoryUtils.add_item_listener,"inv_add")

	@staticmethod
	def add_item_listener(event):
		PlayerConsole.registerNewEvent("success")