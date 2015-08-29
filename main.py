import pygame

from buffalo import utils

from menu import Menu

def main():

    while not utils.end:
        utils.logic()
        utils.update()
        utils.render()
        utils.delta = utils.clock.tick( utils.FRAMES_PER_SECOND )

if __name__ == "__main__":
    
    if not utils.init( 
        logic_func=Menu.logic,
        update_func=Menu.update, 
        render_func=Menu.render,
        ):
        print('buffalo.utils failed to initialize')
        pygame.quit()
        exit()

    main()

    pygame.quit()
