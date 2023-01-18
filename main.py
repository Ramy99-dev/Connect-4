import pygame
from pygame import mixer
from config import *

pygame.init()
mixer.music.load('assets/background-music.mp3')
mixer.music.play(-1)
my_font = pygame.font.SysFont('Cascadia Code', 10)

is_playing = False 
is_over = False



# generate game window

pygame.display.set_caption("Puissance 4")
SCREEN = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
SCREEN.fill(WHITE)

player = 1


running = True
rectangle = []

def drawGrid():
    blockSize = int(WINDOW_WIDTH / 6) #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH+1, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            rectangle.append(rect)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


def gameOver(player):
    SCREEN.fill(BLACK)
    global is_over
    is_over = True
    if(player == 1):
      text_surface = my_font.render('Joueur 1 a gagnier', False, WHITE)
      text_surface = pygame.transform.scale(text_surface,(800,300))
      text_surface_rect= play_button.get_rect()
      text_surface_rect.x = SCREEN.get_width()/7
      SCREEN.blit(text_surface, text_surface_rect)
      
    else:
      text_surface = my_font.render('Joueur 2 a gagnier', False, WHITE)
      text_surface = pygame.transform.scale(text_surface,(800,300))
      text_surface_rect= play_button.get_rect()
      text_surface_rect.x = SCREEN.get_width()/7
      SCREEN.blit(text_surface, text_surface_rect)
  
    SCREEN.blit(play_button,play_button_rect)

            
def checkWinner(matrix):
    length = 0
    for m in matrix:
        for i in range (0 , len(m)):
            if(m[i] == 1):
                length = len(list(filter(lambda x:x==1 , m[i : i+4])))
                if(length == 4):
                    gameOver(1)
                    break
                   
            elif(m[i] == 2):
                length = len(list(filter(lambda x:x==2 , m[i : i+4])))
                if(length == 4):
                    gameOver(2)
                    break
                  
    
    for j in range(0,len(matrix)+1):
        counter = 0
        for i in range(0,len(matrix[j-1])-1):
            if(matrix[i][j] == 1):
                counter +=1
                print(counter)
                if(counter >= 4):
                    print("PLAYER 1 : WINNER")
    
    for j in range(0,len(matrix)+1):
        counter = 0
        for i in range(0,len(matrix[j-1])-1):
            if(matrix[i][j] == 2):
                counter +=1
                print(counter)
                if(counter >= 4):
                    print("PLAYER 2 : WINNER")
                    
        
            

                 

              

def play(matrix):
     global player
     if(matrix[posY][posX] == -1 ):
        if(player == 1):
            pygame.draw.circle(SCREEN,RED,(rectangle[i].x + 50,rectangle[i].y + 50),20)
            matrix[posY][posX] = 1
            checkWinner(matrix)
            player = 2
        else:
            pygame.draw.circle(SCREEN,BLUE,(rectangle[i].x + 50,rectangle[i].y + 50),20)
            matrix[posY][posX] = 2
            checkWinner(matrix)
            player = 1

while running:
    for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    running = False
                    pygame.quit()
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    if play_button_rect.collidepoint(event.pos):
                        is_playing = True  
                        is_over = False    
                        
                        matrix = [[-1,-1,-1,-1,-1,-1,-1],
                                    [-1,-1,-1,-1,-1,-1,-1],
                                    [-1,-1,-1,-1,-1,-1,-1],
                                     [-1,-1,-1,-1,-1,-1,-1],
                                            [-1,-1,-1,-1,-1,-1,-1],
                                            [-1,-1,-1,-1,-1,-1,-1]]
                        SCREEN.fill(WHITE)  
    if is_over == False : 
        if is_playing: 
            drawGrid()
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                
                    for i in range(0,len(rectangle)):
                        if ((rectangle[i].x  < event.pos[0]  < rectangle[i].x + int(WINDOW_WIDTH / 6)) and
                            (rectangle[i].y  < event.pos[1]  < rectangle[i].y + int(WINDOW_HEIGHT/ 6)-60)):
                            posY = int((rectangle[i].y/ 60)-(rectangle[i].y/120)) 
                            posX = int((rectangle[i].x/ 60)-(rectangle[i].x/120)) 
                            
                            if  posY < 0:
                                posY = 0
                            if posX < 0:
                                posX = 0
                            if posY == 5 :  
                                play(matrix)
                            else:
                                if(matrix[posY+1][posX] != -1):
                                    play(matrix)
        else:
            banner = pygame.image.load('assets/logo.png')
            banner_rect = banner.get_rect()
            banner_rect.x = SCREEN.get_width()/5
            SCREEN.blit(banner,banner_rect)

            play_button = pygame.image.load('assets/play-button.png')
            play_button = pygame.transform.scale(play_button,(300,150))
            play_button_rect= play_button.get_rect()
            play_button_rect.x = SCREEN.get_width()/2.9
            play_button_rect.y = SCREEN.get_height()/2
            SCREEN.blit(play_button,play_button_rect)


            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                        running = False
                        pygame.quit()   
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    if play_button_rect.collidepoint(event.pos):
                        is_playing = True  
                        is_over = False    
                        SCREEN.fill(WHITE)     
                
    

    pygame.display.update()

