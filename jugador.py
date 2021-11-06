import pygame
from settings import *

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
        # Cargamos listas y variables con la referencia a nuestro sprites
        self.quieto = pygame.image.load("images/personaje/personaje_quieto.png")

        self.caminarDerecha = [pygame.image.load("images/personaje/run1.png"),
                               pygame.image.load("images/personaje/run2.png"),
                               pygame.image.load("images/personaje/run3.png"),
                               pygame.image.load("images/personaje/run4.png"),
                               pygame.image.load("images/personaje/run5.png"),
                               ]
        self.caminarIzquierda = [pygame.image.load("images/personaje/izq1.png"),
                                 pygame.image.load(
                                     "images/personaje/izq2.png"),
                                 pygame.image.load(
                                     "images/personaje/izq3.png"),
                                 pygame.image.load(
                                     "images/personaje/izq4.png"),
                                 pygame.image.load(
                                     "images/personaje/izq5.png"),
                                 ]

        self.salta = [pygame.image.load("images/personaje/salto1.png"),
                      # pygame.image.load("imagenes/salto2.png"),
                      pygame.image.load("images/personaje/salto3.png")]

    def move(self,keys,pantalla_ancho,pantalla_alto,level):
      
        if keys[pygame.K_LEFT] and self.x >= 0:
            self.x = self.x - self.vel
            self.izquierda = True
            self.derecha = False
            level.move(self.vel)

        elif keys[pygame.K_RIGHT] and self.x < pantalla_ancho - self.vel - self.ancho:
            self.x += self.vel
            self.izquierda = False
            self.derecha = True
            level.move(-self.vel)

        else:
            self.izquierda = False
            self.derecha = False
            self.conteoCaminata = 0

        if not(self.estaSaltando):  # Mientras no salta
         
            if keys[pygame.K_SPACE]:
                self.estaSaltando = True

                self.izquierda = False
                self.derecha = False
                self.conteoCaminata = 0

        else:
            if self.conteoSalto >= -10:
                self.y -= (self.conteoSalto *
                                abs(self.conteoSalto)) * 0.5
                self.conteoSalto -= 1

            else:
                self.conteoSalto = 10
                self.estaSaltando = False
    
 
    def draw(self, pantalla):
        pygame.time.delay(50)
        if self.conteoCaminata + 1 >= 5:
            self.conteoCaminata = 0
        if self.izquierda:
            pantalla.blit(
                self.caminarIzquierda[self.conteoCaminata // 1], (int(self.x), int(self.y)))
            self.conteoCaminata += 1
        elif self.derecha:
            pantalla.blit(
                self.caminarDerecha[self.conteoCaminata // 1], (int(self.x), int(self.y)))
            self.conteoCaminata += 1
        elif self.salto + 1 >= 2:
            pantalla.blit(
                self.salta[self.conteoCaminata // 1], (int(self.x), int(self.y)))
            self.conteoCaminata += 1
        else:
            pantalla.blit(self.quieto, (int(self.x), int(self.y)))
        
       

