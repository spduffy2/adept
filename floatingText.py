import pygame
from buffalo import utils

class FloatingText:
    def __init__(self,text,pos,color=(0,0,0,255),vert_speed=0,hor_speed=0,font_size=15,lifetime=1,alpha_decay=0,bold=False,italic=False,font="comicsans"):
        self.color = color
        self.text = text
        self.pos = pos
        self.vert_speed = vert_speed
        self.hor_speed = hor_speed
        self.lifetime = lifetime
        self.font_size = font_size
        self.alpha_decay = alpha_decay
        self.surface = utils.empty_surface((10, 10))
        self.font = font
        self.italic = italic
        self.bold = bold
        self.lifetime_counter = 0
        self.render()

    def blit(self, dest, pos):
        dest.blit( self.surface, pos )

    def render(self):
        font = pygame.font.SysFont(self.font,self.font_size,bold=self.bold,italic=self.italic)
        text_label_surface = font.render(self.text, True, self.color)
        self.surface = text_label_surface

    def update(self):
        self.pos[0] += hor_speed * utils.delta
        self.pos[1] += vert_speed * utils.delta
        self.color[3] -= self.alpha_decay * utils.delta