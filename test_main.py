from item import Item
import pygame
from buffalo import utils
class TestItem:
    def test_init(self):
        utils.init(
            caption='Adept',
            fullscreen=True
        )
        i = Item("axe")
        assert i.name == "axe"