"""
This module contains the title screen class.

"""

import pygame, constants
from screens.selection_screen import Selection_Screen

class Title_Screen(Selection_Screen):
    """
    A class that that represents the title screen.
    
    This screen displays the options the user may choose.
    
    """
     
    def __init__(self, SCREEN):
        """
        Initializes a title screen object.
        
        """
        Selection_Screen.__init__(self, SCREEN)
    
    def load_music(self):
        """
        This method loads the music.
        
        """
        pygame.mixer.stop()
        pygame.mixer.music.load("music/title.ogg")
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
            self.SCREEN.blit(self.POINTER, (310, 300))
        elif self.option == 4:
            self.SCREEN.blit(self.POINTER, (310, 330))
        elif self.option > 4:
            self.option = 1
            self.SCREEN.blit(self.POINTER, (310, 230))
        elif self.option < 1:
            self.option = 4
            self.SCREEN.blit(self.POINTER, (310, 330))
    
    def draw(self):
        """
        This method draws the background and its respective text 
        onto the screen.
        
        """
        BACKGROUND = pygame.image.load("images/backgrounds/bg_title.png").convert()
        self.SCREEN.blit(BACKGROUND, (0, 0))
        pygame.display.update()
        
        text_title = constants.CALIBRI_48.render("Save the Hero", True, constants.BLACK)
        text_start = constants.CALIBRI_28.render("Start Game", True, constants.BLACK)
        text_story = constants.CALIBRI_28.render("Rules", True, constants.BLACK)
        text_credits = constants.CALIBRI_28.render("Credits", True, constants.BLACK)
        text_quit = constants.CALIBRI_28.render("Quit", True, constants.BLACK)
    
        self.SCREEN.blit(text_title, (270, 150))
        self.SCREEN.blit(text_start, (350, 230))
        self.SCREEN.blit(text_story, (350, 265))
        self.SCREEN.blit(text_credits, (350, 300))
        self.SCREEN.blit(text_quit, (350, 335))