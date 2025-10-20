import pygame

from source.Background import Background
from source.Entity import Entity
from source.Obstacle import Obstacle
from source.Player import Player
from source.const import ENTITY_SPEED, WIN_WIDTH


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Entity):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Obstacle) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def activate_bg_move(ent1, ent2):
        valid_bg_player = False

        if isinstance(ent1, Background) and isinstance(ent2, Player):
            valid_bg_player = True

        if valid_bg_player and ent2.move_bg:





