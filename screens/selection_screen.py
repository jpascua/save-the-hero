"""
This module contains the selection screen class.

"""

import pygame

class Selection_Screen():
    """
    A class that represents the base selection screen.
    
    Attributes:
      option (int): The urrent option the pointer's on.
      selection (int): The selected option.
      SCREEN (Surface): The game's main surface.
      POINTER (Surface): The pointer image.
      
    """
    option = 1
    selection = 0
    SCREEN = None
    POINTER = None
    
    def __init__(self, SCREEN):
        """
        Initializes a selection screen object.
        
        """
        self.SCREEN = SCREEN
        self.POINTER = pygame.image.load("images/other/pointer.png")
        
    def reset_variables(self):
        """
        This method resets the selection number.
        
        """
        self.selection = 0