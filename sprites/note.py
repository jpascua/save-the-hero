"""
This module contains the note sprite class.

"""

import pygame, random

class Note(pygame.sprite.Sprite):
    """
    A class that represents the falling notes.
    
    This class is not mutable.
    
    Attributes:
      image (Surface): Surface of the note.
      rect (Rect): Returns a new rectangle covering the entire image.
      x (int): Initial x-position of the image.
      y (int): Initial y-position of the image.
      speed (int): Speed of note fall by pixel.
    
    """

    def __init__(self, x, y, color, speed):
        """
        Initializes a note object with the given x and y-position, color, and
        speed.
        
        Args:
          x (int): Initial x-position.
          y (int): Initial y-position.
          color (Color): Color of the note.
          speed (int): Speed of note fall by pixel.
        
        """
        super().__init__()
        
        self.image = pygame.Surface((55, 10))
        self.image.fill(color)
                
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def fall(self):
        """
        A method that changes the note's y-position.
        
        """
        self.rect.y += self.speed
        
    @staticmethod
    def generate_note_list(num, color, speed, offset):
        """
        A function that generates a list of notes.
        
        Args:
          num (int): The number of notes to be created.
          color (Color): Color of the note.
          speed (int): Speed of note fall by pixel.
          offset (int): The y-position gap between each note.
          
        Returns:
          List: Populated list.
          
        """
        list_of_notes = []
        
        y = -10
        
        for i in range(num):
            position_id = random.randint(1, 4)
            
            if position_id == 1:
                list_of_notes.append(Note(230, y, color, speed))
            elif position_id == 2:
                list_of_notes.append(Note(330, y, color, speed))
            elif position_id == 3:
                list_of_notes.append(Note(430, y, color, speed))
            elif position_id == 4:
                list_of_notes.append(Note(530, y, color, speed))
            
            y += offset
            
        return list_of_notes