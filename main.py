import pygame, sys
from pygame.locals import * 
from settings import *
from nivel import *
from data_del_juego import nivel_0, nivel_1, nivel_2
from jugador import *
from menu import *

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


corriendo_juego = True 


def runJuego():
    while corriendo_juego:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mmenuBucle = False

        keys = pygame.key.get_pressed()
        dibujar(keys)

        pygame.display.update()
        reloj.tick(30)

opcion=0
menuBucle = True
   
while menuBucle:
    menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                opcion=1
                menuBucle = False
            if event.key == pygame.K_2:
                instrucciones()
                
            
            if event.key == pygame.K_3:
                pygame.display.quit()
                menuBucle = False

if opcion==1:
    runJuego() 
                  
    




''' ##Opcion tecla pulsada
    keys = pygame.key.get_pressed()
    dibujar(keys)

    pygame.display.update()
    reloj.tick(30) '''


        
''' while ejecutar:
    menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_y:
                ##Opcion tecla pulsada
                keys = pygame.key.get_pressed()
                dibujar(keys)

                pygame.display.update()
                reloj.tick(30)
            if event.key == pygame.K_2:
                instrucciones()
            
            if event.key == pygame.K_3:
                pygame.display.quit()
                ejecutar = False
 '''