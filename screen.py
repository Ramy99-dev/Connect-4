from config import  *
import pygame
from pygame import mixer
class Interface():
    
    SCREEN =None
    def __init__(self) :
        self.my_font = pygame.font.SysFont('Cascadia Code', 10)
        pygame.display.set_caption("Puissance 4")
        self.play_button = pygame.image.load('assets/play-button.png')
        self.play_button = pygame.transform.scale(self.play_button,(300,150))
        Interface.SCREEN = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
        Interface.SCREEN.fill(WHITE)

    def gameOver(self,player):
        mixer.music.pause()
        play_button_rect= self.play_button.get_rect()
        Interface.SCREEN.fill(BLACK)
        if(player == 1):
            text_surface =  self.my_font.render('Joueur 1 a gagnier', False, WHITE)
            
        
        elif(player == 2):
            text_surface = self.my_font.render('Joueur 2 a gagnier', False, WHITE)
            
        else:
            text_surface = self.my_font.render('Egalite', False, WHITE)
           

        text_surface = pygame.transform.scale(text_surface,(800,300))
        text_surface_rect= self.play_button.get_rect()
        text_surface_rect.x = Interface.SCREEN.get_width()/7
        play_button_rect.x = Interface.SCREEN.get_width()/2.9
        play_button_rect.y = Interface.SCREEN.get_height()/2
        Interface.SCREEN.blit(text_surface, text_surface_rect)
        Interface.SCREEN.blit(self.play_button,play_button_rect)

    def startScreen(self):
        
        Interface.SCREEN.fill(WHITE)
        banner = pygame.image.load('assets/logo.png')
        banner_rect = banner.get_rect()
        banner_rect.x = Interface.SCREEN.get_width()/5
        Interface.SCREEN.blit(banner,banner_rect)

        
        play_button_rect= self.play_button.get_rect()
        play_button_rect.x = Interface.SCREEN.get_width()/2.9
        play_button_rect.y = Interface.SCREEN.get_height()/2
        Interface.SCREEN.blit(self.play_button,play_button_rect)
       
        return play_button_rect
       

    def getPlayButton(self):
      play_button_rect= self.play_button.get_rect()
      play_button_rect.x = Interface.SCREEN.get_width()/2.9
      play_button_rect.y = Interface.SCREEN.get_height()/2
      return play_button_rect   