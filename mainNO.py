import pygame
import random
pygame.init()


class Pared(pygame.sprite.Sprite):
    def __init__(self):
        super(). __init__()
        self.image = pygame.image.load("Sprites//wall1.png").convert_alpha() #convert_alpha es para la trasparencia
        self.rect = self.image.get_rect() #conversion rectangular


class CREW(pygame.sprite.Sprite):   #Personaje jugable
    def __init__(self):
        super(). __init__()
        self.image = pygame.image.load("Sprites//Elegant_Sir.png").convert_alpha() #convert_alpha es para la trasparencia
        self.rect = self.image.get_rect() #conversion rectangular

class POTION(pygame.sprite.Sprite):
    def __init__(self):
        super(). __init__()
        self.image = pygame.image.load("Sprites//potion.png").convert_alpha() #convert_alpha es para la trasparencia
        self.rect = self.image.get_rect() #conversion rectangular


def mapping(map):
  listaMuros = []
  for cordinate_y, line in enumerate(map):
        #print("y:", cordinate_y, "c:", line)
        for cordinate_x, character in enumerate(line):
            #print("x:", cordinate_x, "cha:", character)
            if character == 0:
              listaMuros.append(pygame.Rect((cordinate_x * projectSize), (cordinate_y * projectSize), projectSize, projectSize))
              pared.rect.x = x
              pared.rect.y = y
              listaPared.add(pared)
              listaPared.draw(ventana)
            #if character == 1:
             #   if random.randint(0, 1):
              #      screen.blit(potion, (cordinate_x * projectSize, cordinate_y * projectSize))
                
            #if character == 2:
             #   if random.randint(0, 1):
              #      screen.blit(pj, (cordinate_x * projectSize, cordinate_y * projectSize))
  print(listaMuros)
  return listaMuros

def RandomPotion ():
    a = random.randrange(2)
    if a == 0:
        print()
    else:
        dibujar_potion()


def dibujar_muro (superficie, rectangulo):
    pygame.draw.rect(superficie, blanco, rectangulo)



def dibujar_mapa (superficie, listaMuros):
    for muro in listaMuros:
        dibujar_muro(superficie, muro)

def dibujar_potion():
    potion.rect.x = x
    potion.rect.y = y
    listaPOTION.add(potion)
    listaPOTION.draw(ventana)

ANCHO = 640
ALTO = 640
p = 0
x = 0
y = 0
hor = 0
ver = 0
mov = pygame.Rect(0, 64, 26, 26)
Fondo = (98, 119, 121)
blanco = (0, 0, 0)
ventana = pygame.display.set_mode((ANCHO, ALTO))
projectSize = 32
#-----Nombre de la ventana-----
icon = pygame.image.load("Sprites//Elegant_Sir.png")
pygame.display.set_caption("Pougus")
pygame.display.set_icon(icon)
#Listas para el uso de las clases

listaPared = pygame.sprite.Group()
pared = Pared()
listaPared.add(pared)
#Segunda lista

listaCREW = pygame.sprite.Group()
crew = CREW()
listaCREW.add(crew)

#Lista Pocion
listaPOTION = pygame.sprite.Group()
potion = POTION()
listaPOTION.add(potion)


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
#Para evadir errores, la lista wall se creara despues de definir las variables del mapa

listaMuros = mapping(map)
p = 0
close = False
while not close:
    for event in pygame.event.get():
        #SALIR DEL JUEGO
        if event.type == pygame.QUIT:
          close = True
        #TECLAS DE MOVIMIENTO
        pygame.key.set_repeat(5)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hor = -1
            elif event.key == pygame.K_RIGHT:
                hor = +1
            elif event.key == pygame.K_UP:
                ver = -1
            elif event.key == pygame.K_DOWN:
                ver = +1
        else:
            hor = 0
            ver = 0
        #mov.x y mov.y son variables creadas para "traducir" a crew.rect, el cual señalara el movimiento del pj
        mov.x += hor
        mov.y += ver

        crew.rect.x = mov.x
        crew.rect.y = mov.y
        #aqui definiremos lo que sucede con el movimiento el tocar una pared
        for muro in listaMuros:
          #print(muro)
          if mov.colliderect(muro):
            mov.x -= hor
            mov.y -= ver
        #COLOR DEL FONDO
        ventana.fill(Fondo)
        #PROGRAMANDO PAREDES
        x = 0
        y = 0
        for fila in map:
            for muro in fila:
                if muro == "0":
                    pass
                #MUROOOOOOOOOOO
                elif muro == "2" and p == 0 :
                    RandomPotion()
                x+=32
            x = 0
            y += 32

    listaCREW.draw(ventana)
    dibujar_mapa(ventana, listaMuros)
    pygame.display.flip()
pygame.quit()