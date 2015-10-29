from buffalo import utils

class Tray(object):

    FEATHER = 2
    # FEATHER is the number of pixels away from the edges of a tray
    # that the "resize region" goes

    DEFAULT_COLOR = (150, 150, 0, 100)

    def __init__(self, pos, size, color=None):
        self.pos = pos
        self.size = size
        self.color = color if color is not None else Tray.DEFAULT_COLOR
        self.surface = utils.empty_surface(self.size)
        self.surface.fill(self.color)

    def resize(self, mouse_pos):
        assert(type(mouse_pos) == tuple and len(mouse_pos) == 2)
        assert(type(mouse_pos[0]) == int and type(mouse_pos[1]) == int)
        x, y = mouse_pos
        # Edges:
        # Left:   0
        # Top:    1
        # Right:  2
        # Bottom: 3
        if x >= self.x - Tray.FEATHER and x <= self.x + self.width + Tray.FEATHER:
            print("YOLO")

    def blit(self, dest):
        dest.blit(self.surface, self.pos)

    @property
    def pos(self):
        return (self.x, self.y)

    @property
    def size(self):
        return (self.width, self.height)

    @property
    def color(self):
        return (self.r, self.g, self.b, self.a)

    @pos.setter
    def pos(self, value):
        assert(type(value) == tuple and len(value) == 2)
        assert(type(value[0]) == int)
        assert(type(value[1]) == int)
        self.x, self.y = value

    @size.setter
    def size(self, value):
        assert(type(value) == tuple and len(value) == 2)
        assert(type(value[0]) == int)
        assert(type(value[1]) == int)
        self.width, self.height = value

    @color.setter
    def color(self, value):
        assert(type(value) == tuple and len(value) == 4)
        assert(type(value[0]) == int and value[0] >= 0 and value[0] <= 255)
        assert(type(value[1]) == int and value[1] >= 0 and value[1] <= 255)
        assert(type(value[2]) == int and value[2] >= 0 and value[2] <= 255)
        assert(type(value[3]) == int and value[3] >= 0 and value[3] <= 255)
        self.r, self.g, self.b, self.a = value
