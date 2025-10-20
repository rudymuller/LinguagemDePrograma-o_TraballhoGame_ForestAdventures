import pygame

from source.Entity import Entity
from source.const import PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, ENTITY_SPEED, WIN_WIDTH, PLAYER_KEY_JUMP, \
    JUMP_SPEED, GRAVITY, FLOOR


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.y_speed += GRAVITY
        self.rect.centery -= self.y_speed

        if self.rect.centery > FLOOR:
            self.rect.centery = FLOOR
            self.jumping = False
        pressed_key = pygame.key.get_pressed()
        # Move Left
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        # Move Right
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
            self.move_bg = True
        else:
            self.move_bg = False

        # Jump
        if pressed_key[PLAYER_KEY_JUMP[self.name]] and not self.jumping:
            self.y_speed = JUMP_SPEED
            self.jumping = True

        pass
