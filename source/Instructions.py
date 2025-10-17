import sys

import pygame
from pygame import Surface, Rect, KEYDOWN, K_ESCAPE
from pygame.font import Font

from source.const import WIN_WIDTH, C_BLACK


class Instructions:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/InstructionsBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def show(self, ):
        pygame.mixer_music.load('./asset/Instructions.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.instructions_text_title(30, 'SINGLE PLAYER:', C_BLACK, (WIN_WIDTH / 2, 30))
        self.instructions_text(20,
                               '-You have to go trough the obstacle and try to reach the end point as faste as '
                               'possible', C_BLACK, (10, 50))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def instructions_text_title(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def instructions_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
