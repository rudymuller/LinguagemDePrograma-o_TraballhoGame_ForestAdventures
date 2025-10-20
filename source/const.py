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
    'Level1Bg0': 3,
    'Level1Bg1': 2,
    'Level1Bg2': 2,
    'Level1Bg3': 2,
    'Level1Bg4': 2,
    'Level1Bg5': 3,
    'Player1': 3,
    'Player2': 3,
    'Obstacle1': 3,
    'Obstacle2': 3,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Player1': 30,
    'Player2': 30,
    'Obstacle1': 50,
    'Obstacle2': 60,
}

# G
GRAVITY = -0.5

# I

INSTRUCTIONS_1PLAYER = ('-You have to go trough the obstacle and try to reach the end point as faste as ''possible',
                        '-Key -> moves the player forward',
                        '-CTRL Right makes the player jump'
                        )

# J
JUMP_HEIGHT = 100
JUMP_SPEED = 10

# M
MENU_OPTION = ('SINGLE PLAYER',
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
