import pygame
from pygame import mixer
from config import *


class Game():
    rectangle = []
    player = 1
    
    SCREEN = None
    def __init__(self):
        pygame.init()
        mixer.music.load('assets/background-music.mp3')
        mixer.music.play(-1)
        self.my_font = pygame.font.SysFont('Cascadia Code', 10)
        pygame.display.set_caption("Puissance 4")
        self.play_button = pygame.image.load('assets/play-button.png')
        self.play_button = pygame.transform.scale(self.play_button,(300,150))
        Game.SCREEN = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
        Game.SCREEN.fill(WHITE)
        
    
    def startScreen(self):
        
        Game.SCREEN.fill(WHITE)
        banner = pygame.image.load('assets/logo.png')
        banner_rect = banner.get_rect()
        banner_rect.x = Game.SCREEN.get_width()/5
        Game.SCREEN.blit(banner,banner_rect)

        
        play_button_rect= self.play_button.get_rect()
        play_button_rect.x = Game.SCREEN.get_width()/2.9
        play_button_rect.y = Game.SCREEN.get_height()/2
        Game.SCREEN.blit(self.play_button,play_button_rect)
       
        return play_button_rect

        
        
    
    def drawGrid(self):
        blockSize = int(WINDOW_WIDTH / 6) #Set the size of the grid block
        for x in range(0, WINDOW_WIDTH+1, blockSize):
            for y in range(0, WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                Game.rectangle.append(rect)
                pygame.draw.rect(Game.SCREEN, BLACK, rect,1)
    
    def gameOver(self,player):
        mixer.music.pause()
        play_button_rect= self.play_button.get_rect()
        Game.SCREEN.fill(BLACK)
        if(player == 1):
            text_surface =  self.my_font.render('Joueur 1 a gagnier', False, WHITE)
            text_surface = pygame.transform.scale(text_surface,(800,300))
            text_surface_rect= self.play_button.get_rect()
            text_surface_rect.x = Game.SCREEN.get_width()/7
            play_button_rect.x = Game.SCREEN.get_width()/2.9
            play_button_rect.y = Game.SCREEN.get_height()/2
            Game.SCREEN.blit(text_surface, text_surface_rect)
        
        elif(player == 2):
            text_surface = self.my_font.render('Joueur 2 a gagnier', False, WHITE)
            text_surface = pygame.transform.scale(text_surface,(800,300))
            text_surface_rect= self.play_button.get_rect()
            text_surface_rect.x = Game.SCREEN.get_width()/7
            play_button_rect.x = Game.SCREEN.get_width()/2.9
            play_button_rect.y = Game.SCREEN.get_height()/2
            Game.SCREEN.blit(text_surface, text_surface_rect)
        else:
            text_surface = self.my_font.render('Egalite', False, WHITE)
            text_surface = pygame.transform.scale(text_surface,(800,300))
            text_surface_rect= self.play_button.get_rect()
            text_surface_rect.x = Game.SCREEN.get_width()/7
            play_button_rect.x = Game.SCREEN.get_width()/2.9
            play_button_rect.y = Game.SCREEN.get_height()/2
            Game.SCREEN.blit(text_surface, text_surface_rect)

  
        Game.SCREEN.blit(self.play_button,play_button_rect)
       
        
    
    def checkWinner(self,matrix):
        length = 0
        for m in matrix:
            for i in range (0 , len(m)):
                if(m[i] == 1):
                    length = len(list(filter(lambda x:x==1 , m[i : i+4])))
                    if(length == 4):
                        self.gameOver(1)
                        return True
                    
                elif(m[i] == 2):
                    length = len(list(filter(lambda x:x==2 , m[i : i+4])))
                    if(length == 4):
                        self.gameOver(2)
                        return True
                        
        for j in range(0,len(matrix)+1):
            counter = 0
            for i in range(0,len(matrix[j-1])-1):
                if(matrix[i][j] == 1):
                    counter +=1
                
                    if(counter == 4):
                        self.gameOver(1)
                        return True
                else:
                    counter = 0
        
        for j in range(0,len(matrix)+1):
            counter = 0
            for i in range(0,len(matrix[j-1])-1):
                if(matrix[i][j] == 2):
                    counter +=1
                    if(counter == 4):
                        self.gameOver(2)
                        return True
                else:
                    counter = 0
                        
        lines = 0
        for m in matrix:
            if(len(list(filter(lambda x : x!=-1 , m)))==7):
                lines +=1
        if lines == 6 :
            self.gameOver(0)
            return True
        
        j = 0
        counter1 = 0
        counter2 = 0
        for k in range (0 , len(matrix)):            
            for i in range (0,len(matrix[k])):
                    if(j < len(matrix[k])-1):
                        if(matrix[j][i] == 1):
                            counter1 +=1
                            counter2 = 0
                            j+=1
                            if counter1 == 4 :
                                self.gameOver(1)
                                return True
                        elif (matrix[j][i] == 2) :
                            counter1 = 0 
                            counter2 +=1   
                            j+=1
                            if counter2 == 4 :
                                self.gameOver(2)
                                return True
            j+=1
            

        j = 0
        counter1 = 0
        counter2 = 0
        for k in range (0 , len(matrix)):            
            for i in range (len(matrix[k])-1 , -1 ,-1):
                    if(j < len(matrix[k])-1):
                        if(matrix[j][i] == 1):
                            counter1 +=1
                            counter2 = 0
                            j+=1
                            if counter1 == 4 :
                                self.gameOver(1)
                                return True
                        elif (matrix[j][i] == 2) :
                            counter1 = 0 
                            counter2 +=1   
                            j+=1
                            if counter2 == 4 :
                                self.gameOver(2)
                                return True
            j+=1
                

                    



                        
    def play(self,matrix,posX,posY,i):
     if(matrix[posY][posX] == -1 ):
        if(Game.player == 1):
            pygame.draw.circle(Game.SCREEN,RED,(Game.rectangle[i].x + 50,Game.rectangle[i].y + 50),20)
            matrix[posY][posX] = 1
            Game.player = 2
            return self.checkWinner(matrix)
            
           
        else:
            pygame.draw.circle(Game.SCREEN,BLUE,(Game.rectangle[i].x + 50,Game.rectangle[i].y + 50),20)
            matrix[posY][posX] = 2
            Game.player = 1
            return self.checkWinner(matrix)
    
    def getPlayButton(self):
      play_button_rect= self.play_button.get_rect()
      play_button_rect.x = Game.SCREEN.get_width()/2.9
      play_button_rect.y = Game.SCREEN.get_height()/2
      return play_button_rect
    
    

    
           
           
    
    def clickOnBlocks(self,event,matrix):
            for i in range(0,len(Game.rectangle)):
                if ((Game.rectangle[i].x  < event.pos[0]  < Game.rectangle[i].x + int(WINDOW_WIDTH / 6)) and
                    (Game.rectangle[i].y  < event.pos[1]  < Game.rectangle[i].y + int(WINDOW_HEIGHT/ 6)-60)):
                    posY = int((Game.rectangle[i].y/ 60)-(Game.rectangle[i].y/120)) 
                    posX = int((Game.rectangle[i].x/ 60)-(Game.rectangle[i].x/120)) 
                    
                    if  posY < 0:
                        posY = 0
                    if posX < 0:
                        posX = 0
                    if posY == 5 :  

                         return self.play(matrix,posX,posY,i)
                    else:
                        if(matrix[posY+1][posX] != -1):
                             return self.play(matrix,posX,posY,i)