import pygame

from buffalo import utils
from buffalo.label import Label
from buffalo.button import Button

class Menu:

    BACKGROUND_COLOR = (25, 150, 25)

    labels = set()
    buttons = set()
    
    @staticmethod
    def init():
        Menu.labels.add(
            Label(
                (5, 5),
                "Adept 0.0 Alpha + 29 August 2015",
            )
        )
        return True

    @staticmethod
    def logic():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                utils.end = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    utils.end = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in Menu.buttons:
                    if button.get_rect().collidepoint( mouse_pos ):
                        button.set_selected(True)
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                for button in Menu.buttons:
                    button.set_selected(False)
                    if button.get_rect().collidepoint( mouse_pos ):
                        if button.func is not None:
                            button.func()

    @staticmethod
    def update():
        pass

    @staticmethod
    def render():
        utils.screen.fill( Menu.BACKGROUND_COLOR )

        for label in Menu.labels:
            label.blit( utils.screen )
        for button in Menu.buttons:
            button.blit( utils.screen )

        pygame.display.update()
