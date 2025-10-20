import pygame

from source.Entity import Entity
from source.const import ENTITY_SPEED, WIN_WIDTH


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT]:
            self.rect.centerx -= ENTITY_SPEED[self.name]
            if self.rect.right <= 0:
                self.rect.left = WIN_WIDTH
            pass

