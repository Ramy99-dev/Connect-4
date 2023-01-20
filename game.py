import pygame
from pygame import mixer
from config import *
from screen import *
from player import *

class Game():
    rectangle = []
    
    
    SCREEN = None
    def __init__(self):
        pygame.init()
        mixer.music.load('assets/background-music.mp3')
        mixer.music.play(-1)
        self.interface = Interface()
        self.player = Player()
        
        
        
    
    def drawGrid(self,SCREEN):
        blockSize = int(WINDOW_WIDTH / 6) #Set the size of the grid block
        for x in range(0, WINDOW_WIDTH+1, blockSize):
            for y in range(0, WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                Game.rectangle.append(rect)
                pygame.draw.rect(SCREEN, BLACK, rect,1)
    
    
        
    
    def checkWinner(self,matrix):
       
        length = 0
        for m in matrix:
            for i in range (0 , len(m)):
                if(m[i] == 1):
                    length = len(list(filter(lambda x:x==1 , m[i : i+4])))
                    if(length == 4):
                        self.interface.gameOver(1)
                        return True
                    
                elif(m[i] == 2):
                    length = len(list(filter(lambda x:x==2 , m[i : i+4])))
                    if(length == 4):
                        self.interface.gameOver(2)
                        return True
                        
        for j in range(0,len(matrix)+1):
            counter = 0
            for i in range(0,len(matrix[j-1])-1):
                if(matrix[i][j] == 1):
                    counter +=1
                
                    if(counter == 4):
                        self.interface.gameOver(1)
                        return True
                else:
                    counter = 0
        
        for j in range(0,len(matrix)+1):
            counter = 0
            for i in range(0,len(matrix[j-1])-1):
                if(matrix[i][j] == 2):
                    counter +=1
                    if(counter == 4):
                        self.interface.gameOver(2)
                        return True
                else:
                    counter = 0
                        
        lines = 0
        for m in matrix:
            if(len(list(filter(lambda x : x!=-1 , m)))==7):
                lines +=1
        if lines == 6 :
            self.interface.gameOver(0)
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
                                self.interface.gameOver(1)
                                return True
                        elif (matrix[j][i] == 2) :
                            counter1 = 0 
                            counter2 +=1   
                            j+=1
                            if counter2 == 4 :
                                self.interface.gameOver(1)
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
                                self.interface.gameOver(1)
                                return True
                        elif (matrix[j][i] == 2) :
                            counter1 = 0 
                            counter2 +=1   
                            j+=1
                            if counter2 == 4 :
                                self.interface.gameOver(2)
                                return True
            j+=1
                

                    
           
    def play(self,matrix,posX,posY,i,SCREEN):
     if(matrix[posY][posX] == -1 ):
        if(self.player.getCurrentPlayer() == 1):
            pygame.draw.circle(SCREEN,RED,(Game.rectangle[i].x + 50,Game.rectangle[i].y + 50),20)
            matrix[posY][posX] = 1
            self.player.switchPlayer()
            return self.checkWinner(matrix)
            
           
        else:
            pygame.draw.circle(SCREEN,BLUE,(Game.rectangle[i].x + 50,Game.rectangle[i].y + 50),20)
            matrix[posY][posX] = 2
            self.player.switchPlayer()
            return self.checkWinner(matrix)
    
   
    
    

    
           
           
    
    def clickOnBlocks(self,event,matrix,SCREEN):
            x  = 0
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
                         return self.play(matrix,posX,posY,i,SCREEN)
                    
                    if(matrix[posY+1][posX] != -1):
                        return self.play(matrix,posX,posY,i,SCREEN)

                    else:
                          
                          while(x + posY <= 5):
                            if(matrix[posY+x][posX] != -1):
                                return self.play(matrix,posX,posY+x-1,x+i-1,SCREEN)
                            else:
                                x+=1
                            if(x + posY == 6):
                                return self.play(matrix,posX,posY+x-1,x+i-1,SCREEN)
                         
                         
                          