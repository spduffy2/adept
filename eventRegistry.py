class EventRegistry:
	EVENTS = list()
	LISTENERS = list()

	@staticmethod
	def registerEvent(event):
		if not isinstance(event, Event):
			raise TypeError
			return
		EventRegistry.EVENTS.append(event)

	@staticmethod
	def getEvents():
		return EventRegistry.EVENTS

	@staticmethod
	def registerListener(listener,_type):
		EventRegistry.LISTENERS.append((listener,_type))

	@staticmethod
	def update():
		#Call the handleEvent() function on all listeners
		for event in EventRegistry.EVENTS:
			for listener in EventRegistry.LISTENERS:
				if listener[1] == event.type:
					if not hasattr(listener, handleEvent):
						print str(listener) + "doesn't have the method \"handleEvent()\""
						raise NotImplementedError
					listener.handleEvent(event)
		#Reset the events list for the next tick
		EventRegistry.EVENTS = list()


class Event:
	def __init__(self, _type="", info = dict()):
		self.type = _type
		self.info = info