import sys

import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.input import Input

from camera import Camera
from pluginManager import PluginManager
from editMapPanel import EditMapPanel

class CameraController:
    def __init__(self):
        self.fPos = (0.0, 0.0)
        self.pos = (int(self.fPos[0]), int(self.fPos[1]))
        self.xv, self.yv = 0.0, 0.0
        self.speed = 1.2
        self.shift_speed = self.speed * 5.0

    def update(self, keys):
        w, a, s, d, shift = (
            keys[pygame.K_w],
            keys[pygame.K_a],
            keys[pygame.K_s],
            keys[pygame.K_d],
            keys[pygame.K_LSHIFT],
        )

        if shift:
            speed = self.shift_speed
        else:
            speed = self.speed

        self.xv = 0.0
        self.yv = 0.0

        if w:
            self.yv -= speed
        if a:
            self.xv -= speed
        if s:
            self.yv += speed
        if d:
            self.xv += speed

        x, y = self.fPos
        x += self.xv
        y += self.yv
        self.fPos = x, y
        self.pos = (int(self.fPos[0]), int(self.fPos[1]))

class EditMapTestScene(Scene):
    def on_escape(self):
        sys.exit()

    def blit(self):
        Camera.blitView()
        utils.screen.blit(self.panel_surface, (utils.SCREEN_W - 180, 10))
        self.tile.fill(self.base_color)
        utils.screen.blit(self.tile, (utils.SCREEN_W - 111, 75))

    def update(self):
        keys = pygame.key.get_pressed()
        self.camera_controller.update(keys)
        Camera.update()

    def __init__(self):
        Scene.__init__(self)
        self.BACKGROUND_COLOR = (0, 0, 0, 255)
        PluginManager.loadPlugins()
        Camera.init()
        self.camera_controller = CameraController()
        Camera.lock(self.camera_controller)

        self.panel_surface = utils.empty_surface((170, utils.SCREEN_H - 20))
        self.panel_surface.fill((255, 255, 255, 100))
        Label.DEFAULT_FONT = "default18"
        Label.DEFAULT_COLOR = (0, 0, 0, 255)
        Input.DEFAULT_FONT = Label.DEFAULT_FONT
        Input.DEFAULT_COLOR = Label.DEFAULT_COLOR
        self.labels.add(
            Label(
                (utils.SCREEN_W - 95, 15),
                "Edit Panel",
                x_centered=True,
                font="default36",
            )
        )
        self.labels.add(
            Label(
                (utils.SCREEN_W - 95, 50),
                "Tile Type",
                x_centered=True,
                font="default24",
            )
        )
        self.tile = utils.empty_surface((32, 32))
        self.labels.add(
            Label(
                (utils.SCREEN_W - 170, 120),
                "Base Color:",
                font="default18",
            )
        )
        self.base_color_b = Input(
            (utils.SCREEN_W - 20, 120),
            "100",
            invert_x_pos=True,
            max_chars=3,
        )
        self.base_color_g = Input(
            (self.base_color_b.label.pos[0] - 5, 120),
            "180",
            invert_x_pos=True,
            max_chars=3,
        )
        self.base_color_r = Input(
            (self.base_color_g.label.pos[0] - 5, 120),
            "255",
            invert_x_pos=True,
            max_chars=3,
        )
        self.mean_temperature = Input(
            (utils.SCREEN_W - 20, 140),
            "100 F",
            invert_x_pos=True,
            max_chars=5,
        )
        self.mean_humidity = Input(
            (utils.SCREEN_W - 20, 160),
            "30%",
            invert_x_pos=True,
            max_chars=3,
        )
        self.mean_nutrient_content = Input(
            (utils.SCREEN_W - 20, 180),
            "100g",
            invert_x_pos=True,
            max_chars=4,
        )
        self.inputs.add(self.base_color_r)
        self.inputs.add(self.base_color_g)
        self.inputs.add(self.base_color_b)
        self.inputs.add(self.mean_temperature)
        self.inputs.add(self.mean_humidity)
        self.inputs.add(self.mean_nutrient_content)
        self.labels.add(
            Label(
                (utils.SCREEN_W - 170, 140),
                "Mean Temperature:",
                font="default18",
            )
        )
        self.labels.add(
            Label(
                (utils.SCREEN_W - 170, 160),
                "Mean Humidity:",
                font="default18",
            )
        )
        self.labels.add(
            Label(
                (utils.SCREEN_W - 170, 180),
                "M. Nutrient Content:",
                font="default18",
            )
        )
        self.last_base_color = (180, 50, 50)

    @property
    def base_color(self):
        r, g, b = self.last_base_color
        # TODO: make three try-excepts and turn the respective text red in each except
        try:
            color = (
            int(self.base_color_r.label.text),
            int(self.base_color_g.label.text),
            int(self.base_color_b.label.text),
            255,
            )
            x, y, z, a = color
            if (x < 0 or x > 255) or (y < 0 or y > 255) or (z < 0 or z > 255):
                raise ValueError
            self.last_base_color = color[:3]
        except:
            color = r, g, b
        return color

    @base_color.setter
    def base_color(self, color):
        r, g, b = color
        self.base_color_r.label.text = str(r)
        self.base_color_g.label.text = str(g)
        self.base_color_b.label.text = str(b)
