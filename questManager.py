from quest import Quest

class QuestManager:
	ACTIVE_QUESTS = list()
	COMPLETED_QUESTS = list()

	@staticmethod
	def update():
		pass

	@staticmethod
	def startQuest(quest):
		quest.onStart()
		QUESTS.append(quest)


