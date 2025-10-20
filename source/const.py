import pygame

# C

C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 128)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_BLACK = (0, 0, 0)

# E
EVENT_OBSTACLE = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0': 2,
    'Level1Bg1': 1,
    'Level1Bg2': 1,
    'Level1Bg3': 1,
    'Level1Bg4': 1,
    'Level1Bg5': 2,
    'Player1': 3,
    'Player2': 3,
    'Obstacle1': 2,
    'Obstacle2': 2,
}

# G
GRAVITY = -0.5

# I

INSTRUCTIONS_1PLAYER = ('-You have to go trough the obstacle and try to reach the end point as faste as ''possible',
                        '-Keys < and > move the player backwards and forwards respectively',
                        '-CTRL Right makes the player jump'
                        )

# J
JUMP_HEIGHT = 100
JUMP_SPEED = 10

# M
MENU_OPTION = ('SINGLE PLAYER',
               '2 PLAYERS',
               'INSTRUCTIONS',
               'EXIT')

# P
PLAYER_KEY_JUMP = {'Player1': pygame.K_RCTRL,
                   'Player2': pygame.K_LCTRL}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 6000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# F
FLOOR = WIN_HEIGHT / 2 + 100
