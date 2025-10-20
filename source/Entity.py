from abc import abstractmethod, ABC

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.y_speed = 0
        self.jumping = False
        self.moving_forward = False


    @abstractmethod
    def move(self, ):
        pass
