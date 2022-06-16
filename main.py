import pygame, random#,sys  
from pygame.locals import *

#ola

size = width, height = 640, 640
#640x640

black = 0, 0, 0
projectSize = 32

map = [
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],

[0,0,2,2,2,2,2,2,0,0,0,1,1,1,1,1,1,1,0,0],

[1,1,2,0,0,0,0,2,0,0,0,1,1,1,1,1,1,1,0,0],

[1,1,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,0,0],

[1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0],
    
[0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,2,2,0],

[0,2,2,2,2,2,2,2,1,1,0,0,1,1,1,1,1,0,2,0],

[0,2,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,2,0],

[0,2,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0],

[0,2,0,0,0,0,0,0,2,0,2,0,0,2,0,0,0,0,0,0],

[0,2,2,2,2,2,2,2,2,0,2,0,0,2,0,1,1,1,1,1],

[0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],

[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,1],

[2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0],

[2,0,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],

[2,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],

[2,0,1,1,1,0,0,1,2,0,2,2,2,0,1,1,1,1,1,0],

[0,0,0,0,0,0,0,0,2,0,2,0,2,0,1,1,1,1,1,0],

[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,0],

[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0]
]

def initialSetup():
    global screen, wall, pj, potion
    screen = pygame.display.set_mode(size)
    wall = pygame.image.load("Sprites//wall1.png")
    pj = pygame.image.load("Sprites//Elegant_Sir.png")
    potion = pygame.image.load("Sprites//potion.png")
    pygame.display.set_caption('PAUGUS')
    pygame.display.set_icon(wall)

def mapping(map):
    global wall
    for cordinate_y, line in enumerate(map):
        #print("y:", cordinate_y, "c:", line)
        for cordinate_x, character in enumerate(line):
            
            print("x:", cordinate_x, "cha:", character)
            if character == 0:
                screen.blit(wall, (cordinate_x * projectSize, cordinate_y * projectSize))
            if character == 1:
                if random.randint(0, 1):
                    screen.blit(potion, (cordinate_x * projectSize, cordinate_y * projectSize))
                
            if character == 2:
                if random.randint(0, 1):
                    screen.blit(pj, (cordinate_x * projectSize, cordinate_y * projectSize))

                
                
 

pygame.init()
initialSetup()
mapping(map)
loop = 1
while loop:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
    pygame.display.update()
pygame.quit()