import pygame

class Tool(object):
    def __init__(self, image_pos, down_image, up_image, selected_image):
        self.image_pos = image_pos
        self.down_image = down_image
        self.up_image = up_image
        self.selected_image = selected_image
        self.image = self.up_image
        self.button_is_down = False
        self.selected = False

    def blit(self, dest):
        dest.blit(self.image, self.image_pos)

    def get_rect(self):
        return pygame.Rect(self.image_pos, (self.image.get_width(),self.image.get_height()))

    @property
    def down(self):
        return self.button_is_down

    @down.setter
    def down(self, value):
        self.button_is_down = value
        if self.button_is_down:
            self.image = self.down_image
        elif self.selected:
            self.image = self.selected_image
        else:
            self.image = self.up_image

    @property
    def selected(self):
        return self.button_is_selected

    @selected.setter
    def selected(self, value):
        self.button_is_selected = value
        if self.selected:
            self.image = self.selected_image
        else:
            self.image = self.up_image
