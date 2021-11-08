import pygame, sys
from pygame.locals import * 
from settings import *
from nivel import *
from data_del_juego import nivel_0, nivel_1, nivel_2
from jugador import *

pygame.init()
pantalla = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))
pygame.display.set_caption('Jumping')

reloj = pygame.time.Clock()
#  FPS SECCION
font = pygame.font.SysFont("Arial", 32)

def update_fps():
	fps = str(int(reloj.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("black"))
	return fps_text


#FIN FPS SECCION

def dibujar(keys):
    nivel_0.run(keys)
    pantalla.blit(update_fps(), (10,0))
    




nivel_0 = Nivel(nivel_0,pantalla)
ejecutar = True

while ejecutar:
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    ##Opcion tecla pulsada
    keys = pygame.key.get_pressed()
    dibujar(keys)

    pygame.display.update()
    reloj.tick(30)

