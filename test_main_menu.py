from buffalo import utils
from menu import Menu
import os
import shutil
from createCharacter import CreateCharacter
utils.init()

class TestMainMenu:
	def test_init(self):
		m = Menu()
		assert m is not None

	def test_load_characters(self):
		m = Menu()
		m.getCharacterNames()

	def test_load_scene_with_no_characters(self):
		m = Menu()
		utils.set_scene(m)
		if os.path.isdir("characters"):
			shutil.rmtree("characters")
		m.getCharacterNames()
		m.go_to_gameTestScene()
		assert utils.scene is m

