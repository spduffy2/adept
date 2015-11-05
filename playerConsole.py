from tray import Tray
from buffalo import utils
import pygame

class PlayerConsole:
    TEXT_EVENTS = list()

    @staticmethod
    def init():
        PlayerConsole.tray = Tray(
            (10,utils.SCREEN_H - utils.SCREEN_H / 4 - 75),
            (utils.SCREEN_W / 2, utils.SCREEN_H / 4),
            color=(100,100,100,200))
        PlayerConsole.TEXT_EVENTS.append(EventText("Hello!"))
        PlayerConsole.TEXT_EVENTS.append(EventText("Hello!"))
        PlayerConsole.TEXT_EVENTS.append(EventText("Hello!"))

    @staticmethod
    def registerNewEvent(text,color=(255,255,255,255)):
        newEvent = EventText(text,color)
        PlayerConsole.TEXT_EVENTS.append(newEvent)

    @staticmethod
    def render():
        totalHeight = 0
        PlayerConsole.tray.update()
        texts = list()
        for textMessage in PlayerConsole.TEXT_EVENTS:
            myfont = pygame.font.SysFont("monospace", 15)
            label = myfont.render(textMessage.text, True, (255,255,255,255))
            texts.append(label)
            totalHeight += label.get_height()

        newSurface = utils.empty_surface((PlayerConsole.tray.surface.get_width(), totalHeight))
        currHeight = 0
        for textSurface in texts:
            newSurface.blit(textSurface,(0,currHeight))
            currHeight += textSurface.get_height()
        PlayerConsole.tray.surface.blit(newSurface,(0,PlayerConsole.tray.surface.get_height() - newSurface.get_height()))

class EventText:
    def __init__(self, text, color=(0,0,0,255)):
        self.text = text
        self.color = color