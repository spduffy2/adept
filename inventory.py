from item import Item

class Inventory():

    def __init__(self):

        self.INV_SIZE_X = 10
        self.INV_SIZE_Y = 3

        self.inventory = [[None]*self.INV_SIZE_X for _ in range(self.INV_SIZE_Y)]
        self.hotbar = [None]*self.INV_SIZE_X

    def addItem(item):
        for x in range(INV_SIZE_X):
            for y in range(INV_SIZE_Y):
                if inventory[x][y] == None and isinstance(item, Item):
                    inventory[x][y] = item
                    return

    def removeItem(item):
        for x in range(INV_SIZE_X):
            for y in range(INV_SIZE_Y):
                if inventory[x][y] == item:
                    inventory[x][y] = None
                    return

    def placeItem(item, x, y):
        if isinstance(item,Item):
            inventory[x][y] = item

    def placeItemInHotbar(item, index):
        if isinstance(item,Item):
            hotbar[index] = item

    def addItemToHotbar(item):
        for x in range(INV_SIZE_X):
            if hotbar[x] == None:
                hotbar[x] = item
                return
