import pygame

pygame.init()

is_playing = False 

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 1080
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE =  (0, 0,255)
RED =  (255, 0, 0)

matrix = [[-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1]]

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
            
def checkWinner(matrix):
    length = 0
    for m in matrix:
        length = len(list(filter(lambda x:(x==1) , m)))
        if(length >=4):
            print("WINNER")
            pygame.quit()
            break

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
        SCREEN.blit(play_button,(0,0))
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                    running = False
                    pygame.quit()                    

                    
                
                  
                   
    pygame.display.update()

