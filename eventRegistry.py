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
	def registerListener(func,_type):
		EventRegistry.LISTENERS.append((func,_type))

	@staticmethod
	def update():
		#Call the handleEvent() function on all listeners
		for event in EventRegistry.EVENTS:
			for listener in EventRegistry.LISTENERS:
				if listener[1] == event.type:
					if listener[0] is not None and callable(listener[0]):
						listener[0](event)
					else:
						print "Error: Could not call " + str(listener[0])
						raise NotImplementedError
		#Reset the events list for the next tick
		EventRegistry.EVENTS = list()


class Event:
	def __init__(self, _type, info):
		if not isinstance(_type,str) or not isinstance(info,dict):
			raise TypeError
			return
		self.type = _type
		self.info = info