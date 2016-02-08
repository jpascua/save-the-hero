"""
This module contains the player score class.

"""

import pygame, constants

class Player_Score():
    """
    This class represents the player's score.
    
    Attributes:
      cool (int): Number of cool timings.
      great (int): Number of great timings.
      perfect (int): Number of perfect timings.
      miss (int): Number of miss timings.
      combo (int): Number of consecutive inputs.
      highest_combo (int): The highest number of consecutive inputs.
      timing (String): Holds either cool, great, perfect, or miss.
      high_scores (List): List of high scores read from the text file.
      SCREEN (Surface): The game's main surface.
      
    """
    SCREEN = None
    
    cool = 0
    great = 0
    perfect = 0
    miss = 0
    combo = 0
    highest_combo = 0
    points = 0
    timing = ""
    high_scores = []
    
    def __init__(self, SCREEN):
        """
        Reads scores from a text file and initializes the a player 
        score object.
        
        Args:
          SCREEN (Surface): The game's main surface.
        
        """
        self.SCREEN = SCREEN
        
        # Read high scores
        file = open("High Scores.txt", "r")
        
        self.high_scores.append(None)
        
        for line in file:
            self.high_scores.append(int(line.strip()))
            
    def write_high_score(self, difficulty_selection):
        """
        This method writes the new high score onto a textfile.
        
        Args:
          difficulty_selection (int): The level number selected.
          
        """
        file = open("High Scores.txt", "w")
        
        if self.points > self.high_scores[difficulty_selection]:
            self.high_scores[difficulty_selection] = self.points
                
        # There is only 3 levels
        for i in range(3):
            if i + 1 == 1:
                file.write(str(self.high_scores[i + 1]))
            else:
                file.write("\n" + str(self.high_scores[i + 1]))
    
    def reset_variables(self):
        """
        This method resets the class's attributes to their initial 
        value 0 or "".
        
        """
        self.cool = 0
        self.great = 0
        self.perfect = 0
        self.miss = 0
        self.combo = 0
        self.highest_combo = 0
        self.points = 0
        self.timing = ""
        
    def draw(self, total_notes):
        """
        This method is responsible for making a simple grade calculation 
        and drawing the score results.
        
        Args:
          total_notes (int): Total number of notes.
        
        """
        successful_notes = self.cool + self.great + self.perfect
        grade = (successful_notes / total_notes) * 100
        
        self.SCREEN.fill(constants.BLACK)
    
        if grade >= 70:
            # Fill with something happier?
            self.SCREEN.blit(pygame.image.load("images/backgrounds/bg_win.png").convert(), (0,0))
            victory_message = "Enemy defeated!"
            color = constants.BLACK
            coordinates = (250, 100)
        else:
            self.SCREEN.blit(pygame.image.load("images/backgrounds/bg_lose.png").convert(), (0,0))
            victory_message = "You have been defeated..."
            color = constants.WHITE
            coordinates = (200, 100)
            
        victory_result = constants.CALIBRI_40.render(victory_message, True, color)
        self.SCREEN.blit(victory_result, coordinates)
      
        cool_result = constants.CALIBRI_28.render("Cool(s): " + str(self.cool), True, color)
        self.SCREEN.blit(cool_result, (320, 150))  
       
        good_result = constants.CALIBRI_28.render("Great(s): " + str(self.great), True, color)
        self.SCREEN.blit(good_result, (320, 180))
        
        perfect_result = constants.CALIBRI_28.render("Perfect(s): " + str(self.perfect), True, color)
        self.SCREEN.blit(perfect_result, (320, 210))
        
        miss_result = constants.CALIBRI_28.render("Miss(s): " + str(self.miss), True, color)
        self.SCREEN.blit(miss_result, (320, 240))
        
        miss_result = constants.CALIBRI_28.render("Highest Combo: " + str(self.highest_combo), True, color)
        self.SCREEN.blit(miss_result, (320, 270))
        
        if grade >= 90:
            letter = "A"
        elif grade < 90 and grade >= 80:
            letter = "B"
        elif grade < 80 and grade >= 70:
            letter = "C"
        elif grade < 70 and grade >= 60:
            letter = "D"
        elif grade < 60:
            letter = "F"
        
        grade_result = constants.CALIBRI_40.render("Grade: " + str(letter), True, color)
        self.SCREEN.blit(grade_result, (300, 320))