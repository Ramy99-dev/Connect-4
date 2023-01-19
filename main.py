import pygame
from pygame import mixer
from config import *
from game import *


game = Game()


is_playing = False 
running = True
is_over = False
play_button_rect = None

while running:
    
          
    if is_over == False : 
        if is_playing: 
            game.drawGrid()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    val = game.clickOnBlocks(event,matrix) 
                    if(val != None):
                        is_over = True
                if(event.type == pygame.QUIT):
                        running = False
                        pygame.quit()

        
        else:
            play_button_rect =  game.startScreen()
            for event in pygame.event.get():
                    if(event.type == pygame.MOUSEBUTTONDOWN):
                        if play_button_rect.collidepoint(event.pos):
                            is_playing = True  
                            is_over = False    
                            Game.SCREEN.fill(WHITE) 
                    if(event.type == pygame.QUIT):
                            running = False
                            pygame.quit()
    else:
        for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                        running = False
                        pygame.quit()   
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    if game.getPlayButton().collidepoint(event.pos):
                        is_playing = True  
                        mixer.music.play(-1)
                        is_over = False   
                        Game.SCREEN.fill(WHITE) 
                        matrix = [[-1,-1,-1,-1,-1,-1,-1],
                                  [-1,-1,-1,-1,-1,-1,-1],
                                  [-1,-1,-1,-1,-1,-1,-1],
                                  [-1,-1,-1,-1,-1,-1,-1],
                                  [-1,-1,-1,-1,-1,-1,-1],
                                  [-1,-1,-1,-1,-1,-1,-1]]
    pygame.display.update()

