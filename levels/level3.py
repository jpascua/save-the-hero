"""
This module contains the third level class.

"""

import pygame, constants
from sprites.note import Note
from levels.level import Level

class Level3(Level):
    """ 
    A class that represents the third level.
    
    This class is not mutable.
    
    Attributes:
      music_length (int): Length of the song in seconds.
      total_notes (int): Total number of notes.
    
    """
    
    def __init__(self, SCREEN):
        """
        Initializes the first level object.
        
        Args:
          SCREEN (Surface): The game's main surface.
          
        """
        Level.__init__(self, SCREEN)
        self.music_length = 143
        self.total_notes = 290
            
    def load_notes(self):
        """
        This method generates a list of notes and adds them into the group.
        
        """
        list_of_notes = Note.generate_note_list(self.total_notes, constants.GREEN, 7, -100)
        
        for note in list_of_notes:
            self.note_sprites.add(note)
            
    def load_enemy_notes(self):
        """
        This method generates a list of enemy notes and adds them into 
        the group.
        
        """
        list_of_notes = Note.generate_note_list(self.total_notes, constants.RED, 9, -150)
        
        for note in list_of_notes:
            self.enemy_note_sprites.add(note)
            
    def load_music(self):
        """
        This method loads the music.
        
        """
        pygame.mixer.stop()
        pygame.mixer.music.load('music/track03.ogg')
        pygame.mixer.music.play()
     
    def draw(self):
        """
        This method draws the background onto the screen.
        
        """
        BACKGROUND = pygame.image.load("images/backgrounds/bg_03.png").convert()
        self.SCREEN.blit(BACKGROUND, (0, 0))