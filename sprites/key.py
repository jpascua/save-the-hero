"""
This module contains the key sprite class.

"""

import pygame

class Key(pygame.sprite.Sprite):
    """
    A class that represents the F, G, H and J keys.
    
    This class draws a mutable invisible key.
    
    Attributes:
      image (Surface): Surface of the invisible key.
      rect (Rect): Returns a new rectangle covering the entire image.
      x (int): Initial x-position of the image.
      y (int): Initial y-position of the image.
      
    """
    
    def __init__(self):
        """
        Initializes a key object with its initial x and y-position.
        
        """
        super().__init__()
        
        self.image = self.image = pygame.Surface((10, 50))

        self.rect = self.image.get_rect()
        self.rect.x = 230
        self.rect.y = 530

    def move(self, x, y):
        """
        A method that moves the key to the given x and y-position.
        
        Args:
          x (int): The x-position.
          y (int): The y-position.
          
        """
        self.rect.x += x
        self.rect.y += y