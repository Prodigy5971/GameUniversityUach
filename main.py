import pygame, random#,sys  
import pygame.mixer as mixer


size = width, height = 640, 640
wallId, obstacleId, potionId, = 0, 1, 2
black = 0, 0, 0
projectSize = 32
loop = 0
maxObstacles = 15
maxPotions = 50

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

walls = []
obstacles = []
potions = []


def initialSetup():
    global loop, screen, clock, wall, pj, pjHitbox, potion, obstacle, player_x, player_y
    
    loop = 1
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    wall = pygame.image.load("Sprites//wall1.png")
    pj = pygame.image.load("Sprites//Elegant_Sir.png")
    pjHitbox = pj.get_rect()
    potion = pygame.image.load("Sprites//potion.png")
    obstacle = pygame.image.load("Sprites//obstacle.png")
    pygame.display.set_caption('PAUGUS')
    pygame.display.set_icon(wall) 
    
    player_x = 0
    player_y = 0

    mixer.init()
    mixer.music.load("Sounds//webi-wabo.mp3")
    mixer.music.set_volume(0.25)
    mixer.music.play()        

def playerInitPosition(map):
    for cordinate_y, line in enumerate(map):
        for cordinate_x, character in enumerate(line):
            print()

def player():
    global player_x, player_y
    screen.blit(pj, (player_x * projectSize, player_y * projectSize), (projectSize, projectSize))
    


def mapping():
    global map, wall, obstacle, potion
    cObstacles = 0
    cPotions = 0
    for cordinate_y, line in enumerate(map):
        #print("y:", cordinate_y, "c:", line)
        for cordinate_x, character in enumerate(line):
            
            #print("x:", cordinate_x, "cha:", character)
            if character == wallId:
                screen.blit(wall, (cordinate_x * projectSize, cordinate_y * projectSize))
                hitbox = pygame.Rect((cordinate_x * projectSize, cordinate_y * projectSize), (projectSize, projectSize))
                walls.append(hitbox)
                    
            if character == obstacleId:
                num = random.randint(0, 4) 
                if num == 1:
                    if(cObstacles > maxObstacles - 1):
                        map[cordinate_y][cordinate_x] = -1
                    else:
                        cObstacles = cObstacles+1
                        screen.blit(obstacle, (cordinate_x * projectSize, cordinate_y * projectSize))
                        hitbox = pygame.Rect((cordinate_x * projectSize, cordinate_y * projectSize), (projectSize, projectSize))
                        obstacles.append(hitbox)
                else:
                    map[cordinate_y][cordinate_x] = -1

            if character == potionId:
                num = random.randint(0, 1)
                if num == 1:
                    if(cPotions > maxPotions - 1):
                       map[cordinate_y][cordinate_x] = -1
                    else:
                        cPotions = cPotions+1                 
                        screen.blit(potion, (cordinate_x * projectSize, cordinate_y * projectSize))
                    hitbox = pygame.Rect(cordinate_x * projectSize, cordinate_y * projectSize, projectSize, projectSize)
                    potions.append(hitbox)
                else:    
                    map[cordinate_y][cordinate_x] = -1


def crash(id, key):
    global potion, wall
    for cordinate_y, line in enumerate(map):
        #print("y:", cordinate_y, "c:", line)
        for cordinate_x, character in enumerate(line):
            if id == 0:
                mov = 0
            #print("x:", cordinate_x, "cha:", character)
            if character == potionId:
                if random.randint(0, 1):
                    screen.blit(potion, (cordinate_x * projectSize, cordinate_y * projectSize))
                    hitbox = pygame.Rect(cordinate_x * projectSize, cordinate_y * projectSize, projectSize, projectSize)
                    potions.append(hitbox)
                    print(map[cordinate_x, cordinate_y])                
            if character == obstacleId:
                if random.randint(0, 1):
                    screen.blit(obstacle, (cordinate_x * projectSize, cordinate_y * projectSize))

                

pygame.init()
initialSetup()
mapping()

def PASS():
    pass


while loop:

    clock.tick(15)
    
    for event in pygame.event.get():
        pygame.key.set_repeat(5)
        
        if event.type == pygame.KEYDOWN:
            collition = bool
            for w in walls:       
                collitionWall = pygame.Rect.colliderect(pjHitbox, w)

            for o in obstacles:
                collitionObstacle = pygame.Rect.colliderect(pjHitbox, o)
                
            for p in potions:
                collitionPotion = pygame.Rect.colliderect(pjHitbox, p)
                
            player()
            if event.key == pygame.K_LEFT:
                crash(0, "left") if collitionWall else print('pass', collition)
                crash(1, "left") if collitionWall else print('pass', collition)
                crash(2, "left") if collitionWall else print('pass', collition)
            elif event.key == pygame.K_RIGHT:
                hor = +1
            elif event.key == pygame.K_UP:
                ver = -1
            elif event.key == pygame.K_DOWN:
                ver = +1
        if event.type == pygame.QUIT:
            loop = 0
    pygame.display.update()
pygame.quit()