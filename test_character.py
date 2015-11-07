from item import Item
import pygame
import unittest
from buffalo import utils

utils.init(
            caption='Adept',
            fullscreen=True
        )

class TestCharacter:
    def init(self):
        from createCharacter import CreateCharacter
        self.c = CreateCharacter()

    def tear_down(self):
        pass

    def test_creation(self):
        self.init()

    def test_saveing(self):
        self.init()
        self.c.characterName.label.text = "Test"
        self.c.create_character()

    def test_surface(self):
        from playerCharacter import PlayerCharacter
        char = PlayerCharacter()
        assert char.surface is not None

    def test_inventory__pc_reference(self):
        from playerCharacter import PlayerCharacter
        char = PlayerCharacter()
        assert char.inventory.playerCharacter() == char
