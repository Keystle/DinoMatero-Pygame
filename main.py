import pygame, sys
from pygame.locals import * 
from settings import *
from nivel import *
from data_del_juego import nivel_0
from jugador import *

pygame.init()
pantalla = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))
pygame.display.set_caption('Jumping')

 
reloj = pygame.time.Clock()

fondo = pygame.image.load("./images/personaje/fondo1.png")
COLOR_FONDO_CLIELO = (76, 131, 216)

def dibujar():
    pantalla.fill(COLOR_FONDO_CLIELO)
    nivel_0.run()
    personaje.draw(pantalla)
    pygame.display.update()

def moviemiento(keys):
    personaje.move(keys,PANTALLA_ANCHO,PANTALLA_ALTO,nivel_0)
    


personaje = Jugador(200, 410, 64, 44)
nivel_0 = Nivel(nivel_0,pantalla)
ejecutar = True

while ejecutar:
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    ##Opcion tecla pulsada
    keys = pygame.key.get_pressed()
    moviemiento(keys)
    dibujar()
