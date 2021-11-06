import pygame, sys
from pygame.locals import * 
from settings import *
from nivel import *
from data_del_juego import nivel_0


pygame.init()
pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))
pygame.display.set_caption('Jumping')

#Cargamos listas y variables con la referencia a nuestro sprites
quieto = pygame.image.load("images/personaje/personaje_quieto.png")

caminarDerecha = [pygame.image.load("images/personaje/run1.png"),
                  pygame.image.load("images/personaje/run2.png"),
                  pygame.image.load("images/personaje/run3.png"),
                  pygame.image.load("images/personaje/run4.png"),
                  pygame.image.load("images/personaje/run5.png"),
                  ]
caminarIzquierda = [pygame.image.load("images/personaje/izq1.png"),
                  pygame.image.load("images/personaje/izq2.png"),
                  pygame.image.load("images/personaje/izq3.png"),
                  pygame.image.load("images/personaje/izq4.png"),
                  pygame.image.load("images/personaje/izq5.png"),
                  ]

salta = [pygame.image.load("images/personaje/salto1.png"), 
         #pygame.image.load("imagenes/salto2.png"),
         pygame.image.load("images/personaje/salto3.png")]


fondo = pygame.image.load("images/personaje/fondo1.png") 
reloj = pygame.time.Clock()
'''
x=50
y=420
ancho=5
alto = 5
vel = 5

clock = pygame.time.Clock()

estaSaltando = False
conteoSalto = 10

#Variables que nos indican la posicion de nuestro personaje
izquierda = False
derecha = False
conteoCaminata = 0
'''

class Jugador(object):
    def __init__(self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.vel = 5
        self.estaSaltando = False
        self.izquierda = False
        self.derecha = False
        self.salto = False
        self.conteoCaminata = 0
        self.conteoSalto = 10

    def draw(self, pantalla):
        if self.conteoCaminata + 1 >= 5:
            self.conteoCaminata = 0
        if self.izquierda:
            pantalla.blit(caminarIzquierda[self.conteoCaminata // 1], (int(self.x), int(self.y)))
            self.conteoCaminata +=1
        elif self.derecha:
            pantalla.blit(caminarDerecha[self.conteoCaminata // 1], (int(self.x), int(self.y)))
            self.conteoCaminata += 1
        elif self.salto + 1 >= 2:
            pantalla.blit(salta[self.conteoCaminata // 1], (int(self.x), int(self.y)))
            self.conteoCaminata += 1
        else:
            pantalla.blit(quieto, (int(self.x), int(self.y)))
        # Actualización de la ventana
        pygame.display.update()

def dibujar():
    pantalla.blit(fondo, (0,0))
    personaje.draw(pantalla)
    pygame.display.update()

personaje = Jugador(200, 410, 64, 44)
ejecutar = True

while ejecutar:
    reloj.tick(27)
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    #Opcion tecla pulsada
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and personaje.x >=0:
        personaje.x = personaje.x - personaje.vel
        personaje.izquierda = True
        personaje.derecha = False

    elif keys[pygame.K_RIGHT] and personaje.x < 500 - personaje.vel - personaje.ancho:
        personaje.x += personaje.vel
        personaje.izquierda = False
        personaje.derecha = True

    else:
        personaje.izquierda = False
        personaje.derecha = False
        personaje.conteoCaminata = 0

    if not(personaje.estaSaltando): #Mientras no salta
        if keys[pygame.K_UP] and personaje.y > personaje.vel:
            personaje.y -= personaje.vel
        if keys[pygame.K_DOWN] and personaje.y < 480 - quieto.get_height():
            personaje.y += personaje.vel

        if keys[pygame.K_SPACE]:
            personaje.estaSaltando = True

            personaje.izquierda = False
            personaje.derecha = False
            personaje.conteoCaminata = 0

    else:
        if personaje.conteoSalto >= -10:
            personaje.y -= (personaje.conteoSalto * abs(personaje.conteoSalto)) * 0.5
            personaje.conteoSalto -= 1
        
        else:
            personaje.conteoSalto = 10
            personaje.estaSaltando = False
    
    dibujar()

pygame.quit()


