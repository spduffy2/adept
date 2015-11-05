from tray import Tray
from buffalo import utils
import pygame

class PlayerConsole:
    TEXT_EVENTS = list()
    ALPHA = 255
    ALPHA_WAIT = 200
    ALPHA_DECAY = 10
    ALPHA_COUNTER = 5001

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
        PlayerConsole.flashOn()

    @staticmethod
    def flashOn():
        PlayerConsole.ALPHA = 255
        PlayerConsole.ALPHA_COUNTER = 0
        PlayerConsole.tray.render()
        PlayerConsole.render()

    @staticmethod
    def update():
        if PlayerConsole.ALPHA is 255:
            PlayerConsole.ALPHA_COUNTER += 1
        if PlayerConsole.ALPHA_COUNTER > PlayerConsole.ALPHA_WAIT and PlayerConsole.ALPHA > 0:
            PlayerConsole.ALPHA -= PlayerConsole.ALPHA_DECAY
            PlayerConsole.render()
        if PlayerConsole.ALPHA < 0:
            PlayerConsole.ALPHA = 0
            PlayerConsole.tray.surface = utils.empty_surface((1,1))
        print PlayerConsole.ALPHA_COUNTER


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
        PlayerConsole.tray.render()
        PlayerConsole.tray.surface.blit(newSurface,(0,PlayerConsole.tray.surface.get_height() - newSurface.get_height()))
        pixels_alpha = pygame.surfarray.pixels_alpha(PlayerConsole.tray.surface)
        pixels_alpha[...] = (pixels_alpha * (PlayerConsole.ALPHA / 255.0))
        del pixels_alpha


class EventText:
    def __init__(self, text, color=(0,0,0,255)):
        self.text = text
        self.color = color