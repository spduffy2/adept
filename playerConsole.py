from tray import Tray
from buffalo import utils

class PlayerConsole:
	TEXT_EVENTS = list()

	@staticmethod
	def init():
		PlayerConsole.tray = Tray(
			(10,10),
			(utils.SCREEN_W / 2, utils.SCREEN_H / 4),
			color=(100,100,100,255))

	@staticmethod
	def registerNewEvent(text,color=(255,255,255,255)):
		newEvent = EventText(text,color)
		PlayerConsole.TEXT_EVENTS.append(newEvent)

	@staticmethod
	def update():
		

class EventText:
	def __init__(self, text, color=(255,255,255,255)):
		this.text = text
		this.color = color