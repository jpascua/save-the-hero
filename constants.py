"""
This module contains the global constants to be shared throughout the program.

"""

import pygame

# Colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(195, 195, 195)
GREEN = pygame.Color(186, 255, 158)
RED = pygame.Color(255, 99, 107)

# Fonts
pygame.init()

CALIBRI_25 = pygame.font.SysFont("Calibri", 25, True, False)
CALIBRI_28 = pygame.font.SysFont("Calibri", 28, True, False)
CALIBRI_40 = pygame.font.SysFont("Calibri", 40, True, False)
CALIBRI_48 = pygame.font.SysFont("Calibri", 48, True, False)
CALIBRI_60 = pygame.font.SysFont("Calibri", 60, True, False)

# Sounds
sound_select = pygame.mixer.Sound("sound/select.ogg")
sound_choose = pygame.mixer.Sound("sound/choose.ogg")
sound_hit = pygame.mixer.Sound("sound/hit.ogg")
sound_slash = pygame.mixer.Sound("sound/slash.ogg")