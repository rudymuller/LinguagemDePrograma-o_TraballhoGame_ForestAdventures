import random

from source.Background import Background
from source.Obstacle import Obstacle
from source.Player import Player
from source.const import WIN_WIDTH, WIN_HEIGHT, FLOOR


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player('Player1', (150, FLOOR))
            case 'Player2':
                return Player('Player2', (150, FLOOR))
            case 'Obstacle1':
                return Obstacle('Obstacle1', (WIN_WIDTH + 10, FLOOR - 40))
            case 'Obstacle2':
                return Obstacle('Obstacle2', (WIN_WIDTH + 10, FLOOR - 30))



