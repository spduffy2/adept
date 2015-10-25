import pygame

from buffalo import utils
from buffalo.label import Label
from buffalo.input import Input

class EditMapPanel(object):
    def __init__(self):
        self.width, self.height = 170, utils.SCREEN_H - 20
        self.pos = (utils.SCREEN_W - self.width - 10, 10)
        self.surface = utils.empty_surface(self.size)
        self.static_labels = set()
        self.inputs = set()
        Label.DEFAULT_FONT = "default18"
        Label.DEFAULT_COLOR = (0, 0, 0, 255)
        Input.DEFAULT_FONT = Label.DEFAULT_FONT
        Input.DEFAULT_COLOR = Label.DEFAULT_COLOR
        self.static_labels.add(
            Label(
                (int(self.width / 2), 10),
                "Edit Panel",
                x_centered=True,
                font="default36",
            )
        )
        self.static_labels.add(
            Label(
                (int(self.width / 2), 50),
                "Tile Type",
                x_centered=True,
                font="default24",
            )
        )
        self.tile = utils.empty_surface((32, 32))
        self.static_labels.add(
            Label(
                (10, 120),
                "Base Color:",
                font="default18",
            )
        )
        self.base_color_b = Input(
            (self.width - 10, 120),
            "50",
            invert_x_pos=True,
        )
        self.base_color_g = Input(
            (self.base_color_b.label.pos[0] - 10, 120),
            "50",
            invert_x_pos=True,
        )
        self.base_color_r = Input(
            (self.base_color_g.label.pos[0] - 10, 120),
            "180",
            invert_x_pos=True,
        )
        self.inputs.add(self.base_color_r)
        self.inputs.add(self.base_color_g)
        self.inputs.add(self.base_color_b)
        self.static_labels.add(
            Label(
                (10, 140),
                "Mean Temperature:",
                font="default18",
            )
        )
        self.static_labels.add(
            Label(
                (10, 160),
                "Mean Humidity:",
                font="default18",
            )
        )
        self.render()

    @property
    def size(self):
        return (self.width, self.height)

    @size.setter
    def size(self, size):
        self.width, self.height = size

    def render(self):
        self.surface.fill((255, 255, 255, 100))
        for label in self.static_labels:
            label.blit(self.surface)
        self.base_color_r.blit(self.surface)
        self.base_color_g.blit(self.surface)
        self.base_color_b.blit(self.surface)
        self.base_color = (
            int(self.base_color_r.label.text),
            int(self.base_color_g.label.text),
            int(self.base_color_b.label.text),
            255,
        )
        self.tile.fill(self.base_color)
        self.surface.blit(self.tile, (int(self.width / 2) - 16, 75))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                for inpt in self.inputs:
                    if inpt.selected:
                        inpt.process_char( event.key )
                        self.render()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                mouse_pos = x - self.pos[0], y - self.pos[1]
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                mouse_pos = x - self.pos[0], y - self.pos[1]
                for inpt in self.inputs:
                    if inpt.get_rect().collidepoint( mouse_pos ):
                        inpt.select()
                        self.render()
                    else:
                        inpt.deselect()
                        self.render()

    def blit(self, dest):
        dest.blit(self.surface, self.pos)
