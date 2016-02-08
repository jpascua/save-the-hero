"""
This module contains the base level class.

"""

import pygame

class Level:
    """ 
    A class that represents the base level.
    
    Attributes:
      note_sprites (Group): Holds the note sprites.
      enemy_note_sprites (Group): Holds the enemy note sprites.
      SCREEN (Surface): The game's main surface.
      music_length (int): Length of the song in seconds.
      total_notes (int): Total number of notes.
    
    """
    
    note_sprites = None
    enemy_note_sprites = None
    SCREEN = None
    music_length = None
    total_notes = None

    def __init__(self, SCREEN):
        """
        Initializes a level object.
        
        Args:
          SCREEN (Surface): The game's main surface.
          
        """
        self.note_sprites = pygame.sprite.Group()
        self.enemy_note_sprites = pygame.sprite.Group()
        self.SCREEN = SCREEN