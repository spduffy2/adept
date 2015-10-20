from serializable import Serializable
class Tile(Serializable):
	def __init__(pos,type_id):
		self.pos = pos
		self.type = type_id

	def loadIDProperties(self):
		pass
