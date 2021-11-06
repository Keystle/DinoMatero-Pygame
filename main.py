import pygame
from pygame.locals import *
from settings import *
from nivel import *
from data_del_juego import nivel_0
from SpritesConMoviemiento import *

pygame.init()
''' pantalla_ancho = 1200
pantalla_alto = 700 '''
screen = pygame.display.set_mode((pantalla_ancho, pantalla_alto))
pygame.display.set_caption('Jumping')
clock = pygame.time.Clock()
nivel = Nivel(nivel_0, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    nivel.run()

    pygame.display.update()
    clock.tick(60)


