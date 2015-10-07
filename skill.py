from serializable import Serializable

class Skill(Serializable):

	DEFAULT_LEVEL = 1
	DEFAULT_EXPERIENCE = 0

	def __init__(self, name, level=None, experience=None, func=None):
		self.level = level if level is not None else Skill.DEFAULT_LEVEL
		self.experience = experience if experience is not None else Skill.DEFAULT_EXPERIENCE

	def gainXP(self, amount):
		self.experience += amount
		if self.experience >= 100*self.level:
			self.level += 1
			self.experience %= (100*self.level)

def doHide(pc):
	pc.color = (100,100,100,100)
hide = Skill("hide")
hide.func = doHide
