from enum import Enum

class Item():
    def __init__(self,_id):
        self.id = _id
        self.info = {
            name : "",
            desc : "",
            droppable : True,
            maxQuantity : 99,
            itemType : ItemType.MISC
            }

class ItemType(Enum):
    WEAPON = 0
    TOOL = 1
    QUEST = 2
    ARMOR = 3
    RESOURCE = 4
    MISC = 5
