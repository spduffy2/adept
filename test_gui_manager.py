from guiManager import GUIManager
from buffalo import utils

utils.init()

def test_init():
	g = GUIManager()

def test_bad_gui_object():
	g = GUIManager()
	g.guiScreens