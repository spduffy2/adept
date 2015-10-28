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

from camera import Camera
from pluginManager import PluginManager

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
