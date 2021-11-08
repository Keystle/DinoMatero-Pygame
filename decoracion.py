import pygame
from settings import CANTIDAD_LOSAS_VERTICALES, TAMANIO_LOSA, PANTALLA_ANCHO, PANTALLA_ALTO


class Cielo:
    def __init__(self, horizonte):
        self.top = pygame.image.load('./images/background/BG1.png').convert_alpha()
        self.bottom = pygame.image.load(
            './images/background/BG3.png').convert_alpha()
        self.middle = pygame.image.load(
            './images/background/BG2.png').convert_alpha()
        self.horizon = horizonte
        self.cielo_x = 0
        # estrechamos las imagenes
        self.top = pygame.transform.scale(
            self.top, (PANTALLA_ANCHO, PANTALLA_ALTO))
        self.bottom = pygame.transform.scale(
            self.bottom, (PANTALLA_ANCHO, PANTALLA_ALTO))
        self.middle = pygame.transform.scale(
            self.middle, (PANTALLA_ANCHO, PANTALLA_ALTO))

    def draw(self, pantalla,movimiento):
            self.cielo_x += movimiento
            pantalla.blit(self.top, (0,0))
            for i in range(0,5):
                pantalla.blit(self.middle, (self.cielo_x*0.2+i*PANTALLA_ANCHO,0))
                pantalla.blit(self.bottom, (self.cielo_x * 0.8+i*PANTALLA_ANCHO,0))

            pantalla.blit(self.middle, (-PANTALLA_ANCHO+self.cielo_x*0.2,0))
            pantalla.blit(self.bottom, (-PANTALLA_ANCHO+self.cielo_x*0.8,0))
            # fondo = pygame.image.load("./images/background/BG3.png").convert_alpha()
            # fondoScale = pygame.transform.scale(fondo,(PANTALLA_ANCHO, PANTALLA_ALTO))

            # x_relativa = self.cielo_x % self.bottom.get_rect().width
            # pantalla.blit(fondoScale, (x_relativa - fondo.get_rect().width, 0))
            # if x_relativa < PANTALLA_ANCHO:
            #     pantalla.blit(fondoScale, (x_relativa, 0))
            # self.cielo_x -=1