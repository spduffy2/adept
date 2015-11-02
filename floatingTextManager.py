from floatingText import FloatingText
from buffalo import utils
from camera import Camera

class FloatingTextManager:
    ACTIVE_FLOATING_TEXTS = list()
    FLOATING_TEXT_SURFACE = utils.empty_surface((utils.SCREEN_W, utils.SCREEN_H))

    @staticmethod
    def update():
        for fText in FloatingTextManager.ACTIVE_FLOATING_TEXTS:
            fText.update()
            if fText.alpha <= 0:
                del fText

    @staticmethod
    def blit(dest, pos):
        FloatingTextManager.render()
        dest.blit( FloatingTextManager.FLOATING_TEXT_SURFACE, (pos) )

    @staticmethod
    def render():
        for fText in FloatingTextManager.ACTIVE_FLOATING_TEXTS:
            fText.render()
            fText.blit(utils.screen,(fText.pos[0] - Camera.pos[0],fText.pos[1] - Camera.pos[1]))