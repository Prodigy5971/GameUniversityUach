import pygame, random#,sys  
import pygame.mixer as mixer


size = width, height = 640, 672
wallId, obstacleId, potionId, = 0, 1, 2
black = 0, 0, 0
projectSize = 32
loop = 0
maxObstacles = 15
maxPotions = 50
velocity = 1
playerDirection = ''
keyDirection = '0'

collitionWall = False
collitionObstacle = False
collitionPotion = False

myPotions = 0


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

map1 = [
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
    global loop, screen, clock, wall, pj, pjHitbox, potion, obstacle, player_x, player_y, font
    
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
    screen.fill((255, 255, 255))
    
    font = pygame.font.Font('freesansbold.ttf', 32)
    
    
    player_x = 0
    player_y = 0

    mixer.init()
    mixer.music.load("Sounds//webi-wabo.mp3")
    mixer.music.set_volume(0.25)
    mixer.music.play()  


def mapping(map):
    global map1, wall, obstacle, potion
    cObstacles = 0
    cPotions = 0
    cBlank = 0
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
                        map1[cordinate_y][cordinate_x] = -1
                    else:
                        cObstacles = cObstacles+1
                        screen.blit(obstacle, (cordinate_x * projectSize, cordinate_y * projectSize))
                        hitbox = pygame.Rect((cordinate_x * projectSize, cordinate_y * projectSize), (projectSize, projectSize))
                        obstacles.append(hitbox)
                else:
                    map1[cordinate_y][cordinate_x] = -1
                    cBlank += 1

            if character == potionId:
                num = random.randint(0, 1)
                if num == 1:
                    if(cPotions > maxPotions - 1):
                       map1[cordinate_y][cordinate_x] = -1
                    else:
                        cPotions = cPotions+1                 
                        screen.blit(potion, (cordinate_x * projectSize, cordinate_y * projectSize))
                        hitbox = pygame.Rect((cordinate_x * projectSize, cordinate_y * projectSize), (projectSize, projectSize))
                        potions.append(hitbox)
                else:    
                    map1[cordinate_y][cordinate_x] = -1
                    cBlank += 1

def updateMap():
    global map1, wall, obstacle, potion
    for cordinate_y, line in enumerate(map1):
        #print("y:", cordinate_y, "c:", line)
        for cordinate_x, character in enumerate(line):
            #print("x:", cordinate_x, "cha:", character)
            if character == wallId:
                screen.blit(wall, (cordinate_x * projectSize, cordinate_y * projectSize))
            if character == obstacleId:
                screen.blit(obstacle, (cordinate_x * projectSize, cordinate_y * projectSize))

            if character == potionId:               
                        screen.blit(potion, (cordinate_x * projectSize, cordinate_y * projectSize))


def playerInitPosition():
    global map1, player_x, player_y
    cBlankSpaces = -1
    num = random.randint(0, 110)#(124-143)
    for cordinate_y, line in enumerate(map1):
        for cordinate_x, character in enumerate(line):
            if character == -1:
                cBlankSpaces += 1
                if num == cBlankSpaces:
                    map1[cordinate_y][cordinate_x] = -2
                    player_x = cordinate_x
                    player_y = cordinate_y
                    player(0, 0)
                
                
def player(x, y):
    global player_x, player_y, pjHitbox, collitionWall, collitionObstacle, collitionPotion, keyDirection
    
    statePotion = False
    
    for w in walls:       
        collitionWall = pygame.Rect.colliderect(pjHitbox, w)

    def direction(d):
        global map1
        if direction != '0':
            if d == 'right' and (map1[player_y][player_x + 1] == 0 or map1[player_y][player_x + 1] == 1):
                print(d)
                return 'stop'
                        
            elif d == 'left' and (map1[player_y][player_x - 1] == 0 or map1[player_y][player_x - 1] == 1):
                print(d)
                return 'stop' 
                        
            elif d == 'up' and (map1[player_y - 1][player_x] == 0 or map1[player_y - 1][player_x] == 1):
                print(d)
                return 'stop' 
                        
            elif d == 'down' and (map1[player_y + 1][player_x] == 0 or map1[player_y + 1][player_x] == 1):
                print(d)
                return 'stop' 
                        
                
    if(direction(keyDirection) == 'stop'):
        keyDirection = '0'
        print('se para*')
        return

    for o in obstacles:
                collitionObstacle = pygame.Rect.colliderect(pjHitbox, o)
                
    for p in potions:
        collitionPotion = pygame.Rect.colliderect(pjHitbox, p)
        if collitionPotion:
            statePotion = True

    if(collitionWall):
        return
        
    if(x != 0 or y != 0):
        if x == 1:
            player_x += velocity
            if statePotion:
                crash(2, "right")
        if x == -1:
            player_x -= velocity
            if statePotion:
                crash(2, "left")
        if y == 1:
            player_y -= velocity
            if statePotion:
                crash(2, "top")
        if y == -1:
            player_y += velocity
            if statePotion:
                crash(2, "down")
                    
def crash(id, key):
    global map1, potion, wall, myPotions
    x = 0
    y = 0
    for cordinate_y, line in enumerate(map1):
        for cordinate_x, character in enumerate(line):
            if id == wallId:
                pass
                
            if id == potionId and player_x == cordinate_x and player_y == cordinate_y:
                if key == 'top':
                    y = -1
                if key == 'down':
                    y = 1
                if key == 'right':
                    x = 1
                if key == 'left':
                    x = -1
                map1[cordinate_y - y][cordinate_x - x] = -1
                myPotions += 1
                #potions.remove(pygame.Rect((cordinate_x * projectSize, cordinate_y * projectSize), (projectSize, projectSize))) 
                

pygame.init()
initialSetup()
mapping(map)
playerInitPosition()

def PASS():
    pass


while loop:
    clock.tick(15)

    #render sprites
    screen.fill((255, 255, 255))
    updateMap()
    screen.blit(pj, (player_x * projectSize, player_y * projectSize))
    
    #render text potion
    rect = pygame.Rect(0,  20 * projectSize, 20 * projectSize, projectSize)
    pygame.draw.rect(screen, black, rect)
    screen.blit(potion, (0 * projectSize, 20 * projectSize))
    text = font.render(str(myPotions), True, (0, 255, 0),(0, 0, 128))
    screen.blit(text, (1 * projectSize, 20 * projectSize))
    
    
    pjHitbox.update((player_x * projectSize, player_y * projectSize), (32, 32))
    
    #pygame.draw.rect(screen, (177, 20, 148), pjHitbox)
    for event in pygame.event.get():
        pygame.key.set_repeat(200, 200)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyDirection = 'left' 
                player(-1, 0)
            
            elif event.key == pygame.K_RIGHT:
                keyDirection = 'right'
                player(1, 0)
          
            elif event.key == pygame.K_UP:
                keyDirection = 'up' 
                player(0, 1)
            
            elif event.key == pygame.K_DOWN:
                keyDirection = 'down' 
                player(0, -1)
                
        if event.type == pygame.QUIT:
            loop = 0
    pygame.display.flip()
    pygame.display.update()
pygame.quit()