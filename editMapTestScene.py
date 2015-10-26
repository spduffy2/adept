import os
import os.path
import sys

import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.input import Input

from camera import Camera
from pluginManager import PluginManager
from editMapPanel import EditMapPanel
from editTool import Tool

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
    def logic(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                utils.end = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.on_escape()
                else:
                    for inpt in self.inputs:
                        if inpt.selected:
                            inpt.process_char( event.key )
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.get_rect().collidepoint( mouse_pos ):
                        button.set_selected(True)
                # IF THE MOUSE IS WITHIN THE TOOLS PART OF THE EDIT PANEL
                x, y = mouse_pos
                if x > utils.SCREEN_W - 180 and x < utils.SCREEN_W - 10 and \
                   y > utils.SCREEN_H - 300 and y < utils.SCREEN_H - 10:
                    for tool in self.tools:
                        if tool.get_rect().collidepoint( mouse_pos ):
                            tool.down = True
                for option in self.options:
                    if option.get_left_rect().collidepoint( mouse_pos ):
                        option.set_left_selected(True)
                        if option.get_right_rect().collidepoint( mouse_pos ):
                            option.set_right_selected(True)
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                for button in self.buttons:
                    button.set_selected(False)
                    if button.get_rect().collidepoint( mouse_pos ):
                        if button.func is not None:
                            button.func()
                # IF THE MOUSE IS WITHIN THE TOOLS PART OF THE EDIT PANEL
                x, y = mouse_pos
                if x > utils.SCREEN_W - 180 and x < utils.SCREEN_W - 10 and \
                   y > utils.SCREEN_H - 300 and y < utils.SCREEN_H - 10:
                    for tool in self.tools:
                        tool.down = False
                        tool.selected = False
                        if tool.get_rect().collidepoint( mouse_pos ):
                            self.selected_tool = tool
                            tool.selected = True
                for inpt in self.inputs:
                    if inpt.get_rect().collidepoint( mouse_pos ):
                        inpt.select()
                    else:
                        inpt.deselect()
                for option in self.options:
                    if option.get_left_rect().collidepoint( mouse_pos ):
                        option.go_left()
                    if option.get_right_rect().collidepoint( mouse_pos ):
                        option.go_right()


    def on_escape(self):
        sys.exit()

    def blit(self):
        Camera.blitView()
        utils.screen.blit(self.panel_surface, (utils.SCREEN_W - 180, 10))
        self.tile.fill(self.base_color)
        utils.screen.blit(self.tile, (utils.SCREEN_W - 111, 75))
        for tool in self.tools:
            tool.blit(utils.screen)

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
        self.panel_surface.fill((255, 100, 0, 150))
        Label.DEFAULT_FONT = "default18"
        Label.DEFAULT_COLOR = (0, 0, 0, 255)
        Input.DEFAULT_FONT = Label.DEFAULT_FONT
        Input.DEFAULT_COLOR = Label.DEFAULT_COLOR
        self.labels.add(
            Label(
                (utils.SCREEN_W - 95, utils.SCREEN_H - 290),
                "Tools",
                x_centered=True,
                font="default24",
            )
        )
        self.labels.add(
            Label(
                (utils.SCREEN_W - 95, utils.SCREEN_H - 270),
                "Area Tool",
                x_centered=True,
                font="default18",
            )
        )
        self.labels.add(
            Label(
                (utils.SCREEN_W - 95, utils.SCREEN_H - 140),
                "Draw Tool",
                x_centered=True,
                font="default18",
            )
        )
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
            (utils.SCREEN_W - 20, 180
         ),
            "100g",
            invert_x_pos=True,
            max_chars=4,
        )
        self.temperature_variance = Input(
            (utils.SCREEN_W - 20, 220),
            "10 F",
            invert_x_pos=True,
            max_chars=5,
        )
        self.humidity_variance = Input(
            (utils.SCREEN_W - 20, 240),
            "10%",
            invert_x_pos=True,
            max_chars=3,
        )
        self.nutrient_content_variance = Input(
            (utils.SCREEN_W - 20, 260),
            "10g",
            invert_x_pos=True,
            max_chars=4,
        )
        self.inputs.add(self.base_color_r)
        self.inputs.add(self.base_color_g)
        self.inputs.add(self.base_color_b)
        self.last_base_color = (255, 180, 100)
        self.inputs.add(self.mean_temperature)
        self.inputs.add(self.mean_humidity)
        self.inputs.add(self.mean_nutrient_content)
        self.inputs.add(self.temperature_variance)
        self.inputs.add(self.humidity_variance)
        self.inputs.add(self.nutrient_content_variance)
        self.labels.add(
            Label(
                (utils.SCREEN_W - 170, 160),
                "Mean Temperature:",
                font="default18",
            )
        )
        self.labels.add(
            Label(
                (utils.SCREEN_W - 170, 180),
                "Mean Humidity:",
                font="default18",
            )
        )
        self.labels.add(
            Label(
                (utils.SCREEN_W - 170, 200),
                "M. Nutrient Content:",
                font="default18",
            )
        )
        self.labels.add(
            Label(
                (utils.SCREEN_W - 170, 240),
                "Temp. Variance:",
                font="default18",
            )
        )
        self.labels.add(
            Label(
                (utils.SCREEN_W - 170, 260),
                "Humidity Variance:",
                font="default18",
            )
        )
        self.labels.add(
            Label(
                (utils.SCREEN_W - 170, 280),
                "Nutrient C. Variance:",
                font="default18",
            )
        )

        #####
        self.tools = list()
        self.tools.append(
            Tool( # This should eventually be a subclass of Tool
                (utils.SCREEN_W - 140, utils.SCREEN_H - 120),
                pygame.image.load(os.path.join("editor_assets", "draw_tool_down.png")),
                pygame.image.load(os.path.join("editor_assets", "draw_tool.png")),
                pygame.image.load(os.path.join("editor_assets", "draw_tool_selected.png")),
            )
        )
        self.tools.append(
            Tool( # This should eventually be a subclass of Tool
                (utils.SCREEN_W - 140, utils.SCREEN_H - 250),
                pygame.image.load(os.path.join("editor_assets", "area_tool_down.png")),
                pygame.image.load(os.path.join("editor_assets", "area_tool.png")),
                pygame.image.load(os.path.join("editor_assets", "area_tool_selected.png")),
            )
        )

    @property
    def base_color(self):
        r, g, b = self.last_base_color
        # TODO: make three try-excepts and turn the respective text red in each except
        try:
            x = int(self.base_color_r.label.text)
            if (x < 0 or x > 255):
                raise ValueError
            self.base_color_r.label.color = (0, 0, 0, 255)
            self.base_color_r.label.render()
        except:
            self.base_color_r.label.color = (255, 0, 0, 255)
            self.base_color_r.label.render()
            x = r
        try:
            y = int(self.base_color_g.label.text)
            if (y < 0 or y > 255):
                raise ValueError
            self.base_color_g.label.color = (0, 0, 0, 255)
            self.base_color_g.label.render()
        except:
            self.base_color_g.label.color = (255, 0, 0, 255)
            self.base_color_g.label.render()
            y = g
        try:
            z = int(self.base_color_b.label.text)
            if (z < 0 or z > 255):
                raise ValueError
            self.base_color_b.label.color = (0, 0, 0, 255)
            self.base_color_b.label.render()
        except:
            self.base_color_b.label.color = (255, 0, 0, 255)
            self.base_color_b.label.render()
            z = b
        color = x, y, z, 255
        self.last_base_color = color[:3]
        return color

    @base_color.setter
    def base_color(self, color):
        r, g, b = color
        self.base_color_r.label.text = str(r)
        self.base_color_g.label.text = str(g)
        self.base_color_b.label.text = str(b)
