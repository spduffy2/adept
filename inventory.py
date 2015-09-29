from item import Item

class Inventory():
    INV_SIZE_X = 15
    INV_SIZE_Y = 6

    def __init__(self):
        self.inventory = [[None]*INV_SIZE_X for _ in range(INV_SIZE_Y)]
        self.hotbar = [None]*INV_SIZE_X
