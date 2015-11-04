import os
import os.path
import sys

import numpy
import numpy.random

import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.input import Input

from editMapTestScene import CameraController
from pluginManager import PluginManager
from tray import Tray
from subMap import SubMap

class EditSubMapTestScene(Scene):
    def on_escape(self):
        self.subMap.toFile()
        sys.exit()

    def blit(self):
        #RenderSubmap
        for tray in self.trays:
            tray.blit(utils.screen)

    def update(self):
        keys = pygame.key.get_pressed()
        self.camera_controller.update(keys)
        Camera.update()
        if self.mouse_buttons[0]:
            for tray in self.trays:
                tray.handle(self.mouse_pos, self.mouse_rel)
        else:
            for tray in self.trays:
                tray.should_move = False
                tray.should_resize = False
                tray.edge = 0b0000

    def __init__(self,_id):
        Scene.__init__(self)
        self.subMap = SubMap(_id)
        self.BACKGROUND_COLOR = (0, 0, 0, 255)
        PluginManager.loadPlugins()
        Camera.init()
        self.camera_controller = CameraController()
        Camera.lock(self.camera_controller)
        self.trays = set()
        self.trays.add(
            Tray(
                (utils.SCREEN_W - 270, 20),
                (250, 800),
                min_width=250, max_width=800,
                min_height=250, max_height=800
            )
        )