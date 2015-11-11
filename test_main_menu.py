from buffalo import utils
from menu import Menu
utils.init()

class TestMainMenu:
	def test_init(self):
		m = Menu()
		assert m is not None