import pygame
from settings import *

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        """ self.rect = self.image.get_rect(topleft = pos) """
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.vel = 10
        self.direccion = pygame.math.Vector2(0,0)
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
                       pygame.image.load("images/personaje/salto2.png"),
                      pygame.image.load("images/personaje/salto3.png")]

        

    def move(self,keys):
        localX = self.x
        if keys[pygame.K_LEFT] | keys[pygame.K_a]:
            self.direccion.x = 1
            self.x = self.x - self.vel
            self.izquierda = True
            self.derecha = False
           

        elif keys[pygame.K_RIGHT] | keys[pygame.K_d] :
            self.direccion.x = -1
            self.x += self.vel
            self.izquierda = False
            self.derecha = True
           

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
                self.y -= (self.conteoSalto *abs(self.conteoSalto)) * 0.5
                self.conteoSalto -= 1

            else:
                self.conteoSalto = 10
                self.estaSaltando = False
        return localX - self.x
 
    def draw(self, pantalla):
        if self.conteoCaminata + 1 >= 5:
            self.conteoCaminata = 0
        if self.izquierda:
            pantalla.blit(
                self.caminarIzquierda[self.conteoCaminata // 1], (PANTALLA_ANCHO/2,int(self.y)))
            self.conteoCaminata += 1
        elif self.derecha:
            pantalla.blit(
                self.caminarDerecha[self.conteoCaminata // 1], (PANTALLA_ANCHO/2,int(self.y)))
            self.conteoCaminata += 1
        elif self.salto:
            pantalla.blit(
                self.salta[self.conteoCaminata // 1], (PANTALLA_ANCHO/2,int(self.y)))
            self.conteoCaminata += 1
        else:
            pantalla.blit(self.quieto, (PANTALLA_ANCHO/2,int(self.y)))
        
       

