from buffalo import utils
import pygame

class GUIManager:
	def __init__(self):
		self.active = False;
		self.surface = utils.empty_surface((utils.SCREEN_W, utils.SCREEN_H))
		self.guiScreens = list()
		self.keydown = False;
		self.mousedown = False;

	def updateGUIs(self):
		self.surface = utils.empty_surface((utils.SCREEN_W, utils.SCREEN_H))
		for UIObject in self.guiScreens:
			UIObject.update()
			self.surface.blit(UIObject.surface, UIObject.pos)

	def findCollidingGUI(self, pos):
		for UIObject in self.guiScreens:
			guiPos = UIObject.pos
			guiRect = pygame.Rect(guiPos, (UIObject.surface.get_size()))
			if guiRect.collidepoint(pos):
				return UIObject
		return None


	def update(self):
		#Keyboard Events
		keys = pygame.key.get_pressed()
		if keys[pygame.K_e]:
			#On Keydown
			if not self.keydown:
				self.active = not self.active
				self.keydown = True
		else:
			self.keydown = False

		#Mouse Events
		if not self.active:
			return
		if pygame.mouse.get_pressed()[0]:
			#On Mousedown
			if not self.mousedown:
				self.mousedown = True
				UIObject = self.findCollidingGUI(pygame.mouse.get_pos())
				if UIObject != None:
					UIObject.mouseDown(pygame.mouse.get_pos())
					self.updateGUIs()

		else:
			self.mousedown = False

	

	def blit(self, dest, pos):
		if(self.active):
			#self.updateGUIs()
			dest.blit(self.surface, pos)