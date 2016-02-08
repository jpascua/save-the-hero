"""
This module is responsible for starting the game.

"""

import pygame, sys
from pygame.locals import *
from sprites.key import Key
import constants, player_score
from screens.title_screen import Title_Screen
from screens.difficulty_screen import Difficulty_Screen
from levels.level1 import Level1
from levels.level2 import Level2
from levels.level3 import Level3

def main():
    """
    This function initializes essential game properties and starts the 
    main game loop.
    
    """
    # ===================== Main Set-Up ===================== #
    pygame.init()
    
    FPS = 30
    frame_count = 0
    FPS_CLOCK = pygame.time.Clock()
    
    RESOLUTION = (800, 600)
    SCREEN = pygame.display.set_mode(RESOLUTION)
        
    pygame.display.set_caption("Save the Hero")
    
    pygame.mouse.set_visible(False)
    
    # ===================== Sprite Set-Up ===================== #
    key = Key()
    
    # ===================== Other ===================== #
    level_list = []
    level_list.append(None)  # Needed for indexing!
    level_list.append(Level1(SCREEN))
    level_list.append(Level2(SCREEN))
    level_list.append(Level3(SCREEN))
    
    title = Title_Screen(SCREEN)
    
    title.load_music()
    title.draw()
    SCREEN.blit(title.POINTER, (310, 230))
    
    difficulty = Difficulty_Screen(SCREEN)
    score = player_score.Player_Score(SCREEN)
    
    f_glow = False
    g_glow = False
    h_glow = False
    j_glow = False

    difficulty_screen_flag = False
    gameplay_screen_flag = False
    results_screen_flag = False
    initialization_flag = False
    
    # ===================== Start of Main Game Loop ===================== #
    while True:
        # Reset position of key
        key.rect.x = 0
            
        # ===================== Start of Key Listener ===================== # 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
            # ===================== Menu Controls ===================== #
                if title.selection != 0:
                    # Returns to title screen
                    if event.key == K_ESCAPE:   
                        title.load_music()
                        title.draw()
                        
                        # Reset values
                        frame_count = 0
                         
                        score.reset_variables()
                        title.reset_variables()
                        difficulty.reset_variables()
                        
                        title.draw_pointer()
                         
                        gameplay_screen_flag = False
                        results_screen_flag = False
            
                if (title.selection == 0 or title.selection == 1 and 
                    difficulty.selection == 0):
                    # FOR MENU SELECTIONS ONLY!
                    if event.key == K_DOWN:
                        constants.sound_select.play()
                        # Title screen
                        if title.selection == 0:
                            title.option += 1
                            title.draw()
                            title.draw_pointer()
                        # Difficulty screen
                        elif title.selection == 1:
                            difficulty.option += 1
                            difficulty.draw()
                            difficulty.draw_pointer()
                    if event.key == K_UP:
                        constants.sound_select.play()             
                        # Title screen
                        if title.selection == 0:
                            title.option -= 1
                            title.draw()
                            title.draw_pointer()
                        # Difficulty screen
                        elif title.selection == 1:
                            difficulty.option -= 1
                            difficulty.draw()
                            difficulty.draw_pointer()
                    if event.key == K_RSHIFT:
                        if difficulty.selection == 0:
                        # No level was selected
                            constants.sound_choose.play()
                            if title.selection == 0:
                            # Title screen
                                title.selection = title.option
    
                                if title.selection == 1:
                                    difficulty_screen_flag = True
                            elif title.selection == 1:
                            # Difficulty screen
                                difficulty.selection = difficulty.option
                                
                                gameplay_screen_flag = True
                                initialization_flag = True
            
            # ===================== End of Menu Controls ===================== #
                
            # ===================== Game Controls ===================== # 
                if difficulty.selection != 0:
                # A track is selected
                    if event.key == K_f:
                        key.rect.x = 230
                        f_glow = True
                    if event.key == K_g:
                        key.rect.x = 330
                        g_glow = True
                    if event.key == K_h:
                        key.rect.x = 430
                        h_glow = True
                    if event.key == K_j:
                        key.rect.x = 530
                        j_glow = True
                        
            if event.type == KEYUP:
                if difficulty.selection != 0:
                    if event.key == K_f:
                        f_glow = False
                    if event.key == K_g:
                        g_glow = False
                    if event.key == K_h:
                        h_glow = False
                    if event.key == K_j:
                        j_glow = False
            # ===================== End of Game Controls ===================== #
                                    
        # ===================== End of Key Listener ===================== #
        
        # Process selections
        if title.selection == 1:    
            if difficulty_screen_flag:
                difficulty.draw()
                SCREEN.blit(difficulty.POINTER, (310, 230))
                
                difficulty_screen_flag = False
        if title.selection == 2:
            SCREEN.blit(pygame.image.load("images/other/rules.png").convert(), 
                        (0,0))
        elif title.selection == 3:
            SCREEN.blit(pygame.image.load("images/other/credits.png").convert(), 
                        (0,0))
        elif title.selection == 4:
            pygame.quit()
            sys.exit()

        # ===================== Start of Game ===================== #
        if gameplay_screen_flag:
            # One instance of the game
            if initialization_flag:
                # Empty the group of sprites
                level_list[difficulty.selection].note_sprites.empty()
                level_list[difficulty.selection].enemy_note_sprites.empty()
                # Generate a new list of notes
                level_list[difficulty.selection].load_notes()
                level_list[difficulty.selection].load_music()
                level_list[difficulty.selection].load_enemy_notes()
                
                hit = (pygame.image.load("images/other/hit.png")\
                       .convert_alpha())
                slash = (pygame.image.load("images/other/slash.png")
                        .convert_alpha())

                initialization_flag = False
            
            level_list[difficulty.selection].draw()
         
            if f_glow:
                letter_f = constants.CALIBRI_60.render("F", True, 
                                                       constants.GREY)
                SCREEN.blit(letter_f, (244, 544))
            if g_glow:
                letter_g = constants.CALIBRI_60.render("G", True, 
                                                       constants.GREY)
                SCREEN.blit(letter_g, (338, 544))
            if h_glow:
                letter_h = constants.CALIBRI_60.render("H", True, 
                                                       constants.GREY)
                SCREEN.blit(letter_h, (438, 544))
            if j_glow:
                letter_j = constants.CALIBRI_60.render("J", True, 
                                                       constants.GREY)
                SCREEN.blit(letter_j, (548, 543))
         
            # Move NORMAL notes
            for note in level_list[difficulty.selection].note_sprites:
                note.fall()
                # Notes that fall out of the screen
                if note.rect.y > 600:
                    level_list[difficulty.selection].note_sprites.remove(note)
                    score.timing = "MISS"
                    score.miss += 1
                    
                    constants.sound_hit.play()          
                    SCREEN.blit(hit, (400, 100))

                    score.combo = 0
                   
            note_hit_list = (pygame.sprite.spritecollide
                            (key, level_list[difficulty.selection].note_sprites, 
                             True))
 
            # Timing calculation!
            for note in note_hit_list:
                if (note.rect.y == 530):
                    score.timing = "PERFECT"
                    score.points += 3
                    score.perfect += 1
                elif (note.rect.y > 530 and note.rect.y <= 550):
                    score.timing = "GREAT"
                    score.points += 2
                    score.great += 1
                elif (note.rect.y > 550 and note.rect.y <= 580):
                    score.timing = "COOL"
                    score.points += 1
                    score.cool += 1
                    
                score.combo += 1
                
                if score.combo > score.highest_combo:
                    score.highest_combo = score.combo
                    
                constants.sound_slash.play()          
                SCREEN.blit(slash, (-100, 200))
                
            # Move ENEMY notes      
            for note in level_list[difficulty.selection].enemy_note_sprites:
                note.fall()
                
                if note.rect.y > 550:
                    (level_list[difficulty.selection]
                     .enemy_note_sprites.remove(note))

            enemy_note_hit_list = (pygame.sprite.spritecollide
                                   (key, level_list[difficulty.selection]
                                    .enemy_note_sprites, True))
            
            if enemy_note_hit_list:
                gameplay_screen_flag = False
                results_screen_flag = True
                    
            # Timer
            total_seconds = (level_list[difficulty.selection].music_length - 
                            (frame_count // FPS))
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            time_string = "Time Left: {0:02}:{1:02}".format(minutes, seconds)
            
            if total_seconds < 0:
                total_seconds = 0
                    
            # Draw score and timing
            draw_text(SCREEN, "High Score: " + 
                      str(score.high_scores[difficulty.selection]), 620, 20)
            draw_text(SCREEN, "Points: " + str(score.points), 620, 50)
            draw_text(SCREEN, time_string, 20, 20)
            
            timing = constants.CALIBRI_48.render(score.timing, True, 
                                                 constants.WHITE)
            SCREEN.blit(timing, (350, 150))
            
            if score.combo != 0 and score.timing != "":
                combo = constants.CALIBRI_40.render(str(score.combo) + "x", 
                                                    True, constants.WHITE)
                SCREEN.blit(combo, (370, 200))
             
            # Draw the notes
            level_list[difficulty.selection].note_sprites.draw(SCREEN)
            level_list[difficulty.selection].enemy_note_sprites.draw(SCREEN)
            
            if results_screen_flag:
                score.draw(level_list[difficulty.selection].total_notes)
                score.write_high_score(difficulty.selection)
                gameplay_screen_flag = False  
            
            if (total_seconds == 0):
                results_screen_flag = True
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        # Count frames to calculate total seconds
        frame_count += 1
        FPS_CLOCK.tick(FPS)
                
        pygame.display.update()
        
        # ===================== End of Game ===================== #
        
    # ===================== End of Main Game Loop ===================== #
    
def draw_text(SCREEN, text, x, y):
    """
    This function draws text onto the screen with the given
    x and y coordinates.
    
    Args:
      SCREEN (Surface): The game's main surface.
      text (String): The string to be drawn.
      x (int): The x-position.
      y (int): The y-position.
      
    """
    text = constants.CALIBRI_25.render(text, True, constants.BLACK)
    SCREEN.blit(text, (x, y))
    
if __name__ == '__main__':
    main()