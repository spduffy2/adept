class Serializable: #Converts objects into strings and vice versa

	#Anything that needs to be saved should extend this or extend something that extends this

	def serialize(self): #Converts the object into a dictionary so it can be json encoded
		d = { '__class__':self.__class__.__name__, 
			'__module__':self.__module__,
			}
		d.update(self.__dict__)
		return d

	@staticmethod
	def deserialize(d): #Takes a dictionary (Presumably one that was encoded as per above) and uses it to create an object
		if '__class__' in d:
			class_name = d.pop('__class__')
			module_name = d.pop('__module__')
			module = __import__(module_name)
			class_ = getattr(module, class_name)
			args = dict( (key, value) for key, value in d.items())
			inst = class_(**args)
		else:
			inst = d
		return inst
