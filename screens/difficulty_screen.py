"""
This module contains the difficulty screen class.

"""

import pygame, constants
from screens.selection_screen import Selection_Screen
        
class Difficulty_Screen(Selection_Screen):
    """
    A class that represents the difficulty screen.
    
    This screen displays the different levels the user can choose.
    
    """
    
    def __init__(self, SCREEN):
        """
        Initializes a difficult screen object.
        
        """
        Selection_Screen.__init__(self, SCREEN)
        
    def reset_variables(self):
        """
        This method overrides the super class's reset_variables method.
        It resets the current option and selection number.
        
        """
        self.option = 1
        self.selection = 0
    
    def load_music(self, track_selection):
        """
        This method loads the music.
        
        """
        pygame.mixer.stop()
            
        if track_selection == 1:
            pygame.mixer.music.load("music/track01.ogg")
        elif track_selection == 2:
            pygame.mixer.music.load("music/track02.ogg")     
            
        pygame.mixer.music.play()
        
    def draw_pointer(self):
        """
        This method draws the pointer at its respective position depending
        on the option number onto the screen.
        
        """
        if self.option == 1:
            self.SCREEN.blit(self.POINTER, (310, 230))
        elif self.option == 2:
            self.SCREEN.blit(self.POINTER, (310, 260))
        elif self.option == 3:
            self.SCREEN.blit(self.POINTER, (310, 295))
        elif self.option > 3:
            self.option = 1
            self.SCREEN.blit(self.POINTER, (310, 230))
        if self.option < 1:
            self.option = 3
            self.SCREEN.blit(self.POINTER, (310, 295))
            
    
    def draw(self):
        """
        This method draws the background and its respective text 
        onto the screen.
        
        """
        BACKGROUND = pygame.image.load("images/backgrounds/bg_difficulty.png").convert()
        self.SCREEN.blit(BACKGROUND, (0, 0))
        pygame.display.update()
        
        text_title = constants.CALIBRI_48.render("Select a Difficulty", True, constants.BLACK)
        text_level1 = constants.CALIBRI_28.render("Level 1", True, constants.BLACK)
        text_level2 = constants.CALIBRI_28.render("Level 2", True, constants.BLACK)
        text_level3 =constants. CALIBRI_28.render("Level 3", True, constants.BLACK)
        
        self.SCREEN.blit(text_title, (250, 150))
        self.SCREEN.blit(text_level1, (350, 230))
        self.SCREEN.blit(text_level2, (350, 265))
        self.SCREEN.blit(text_level3, (350, 300))