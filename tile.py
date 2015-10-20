from serializable import Serializable
from buffalo import utils
from subMap import SubMap

class Tile(Serializable):
	def __init__(pos,type_id):
		self.pos = pos
		self.type = type_id
		self.surface = utils.empty_surface((SubMap.TILE_SIZE,SubMap.TILE_SIZE))

	def loadIDProperties(self):
		pass