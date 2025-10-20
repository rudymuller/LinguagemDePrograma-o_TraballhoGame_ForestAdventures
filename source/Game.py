import pygame

from source.Instructions import Instructions
from source.Level import Level
from source.Menu import Menu
from source.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            instructions = Instructions(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTION[1]:
                instructions.show()

            elif menu_return == MENU_OPTION[3]:
                pygame.quit()  # Close window
                quit()  # end pygame
                pass
