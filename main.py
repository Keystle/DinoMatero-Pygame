import pygame, sys
from pygame.locals import * 
from settings import *
from nivel import *
from data_del_juego import nivel_0, nivel_1, nivel_2
from jugador import *
from menu import *

pygame.init()

# class Moneda:
#     def __init__(self): 
#         self.coins = 0
#     def add_coin(self,amount):
#         self.coins += amount

class Main:
    def __init__(self):
        # MUSICA
        self.musica_fondo = pygame.mixer.Sound("audio/overworld_music.wav")
        self.musica_fondo.set_volume(0.2)
        self.musica_fondo.play(-1)

        self.opcionMenu = -1
        self.monedas=0
        self.corriendo_juego = True
        self.niveles = [nivel_0, nivel_1, nivel_2]
        self.numeroNivelActual = 0

        self.crearPantalla()
        self.crearFps()
        self.niveles_juegos = []
        for i in range(len(self.niveles)):
            self.niveles_juegos.append(Nivel(self.niveles[i],self.pantalla, self.monedas))

            
        self.nivelActual =self.niveles_juegos[self.numeroNivelActual]
        self.mostrarMenu()



    def crearPantalla(self):
        self.pantalla = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))
        pygame.display.set_caption('Jumping')

    def crearFps(self):
        self.reloj = pygame.time.Clock()
#     FPS SECCION
        self.font = pygame.font.SysFont("Arial", 32)


    def update_fps(self):
        fps = str(int(self.reloj.get_fps()))
        fps_text = self.font.render(fps, 1, pygame.Color("black"))
        return fps_text

    def mostrarMenu(self):
        corriendo=True
        while corriendo:
            menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_1:
                        self.opcionMenu=1
                        corriendo=False
                    if event.key == pygame.K_2:
                        self.opcionMenu=2
                    if event.key == pygame.K_3:
                        self.opcionMenu=3
                        corriendo=False
            if self.opcionMenu==2:
                instrucciones()
            

        if self.opcionMenu==1:
            self.runJuego()
        elif self.opcionMenu==3:
            pygame.display.quit()

            

    
    def dibujar(self):
        self.nivelActual.run()
        self.pantalla.blit(self.update_fps(), (10,0))  
            
    def runJuego(self):
        
        while self.corriendo_juego:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.corriendo_juego = False

            self.dibujar()
            if(self.nivelActual.finNivel):
                self.monedas = self.nivelActual.monedas
                self.numeroNivelActual = self.numeroNivelActual+1
                """ if self.numeroNivelActual == 3:
                    self.numeroNivelActual = 0
                    for i in range(len(self.niveles)):
                        self.niveles_juegos.(Nivel(self.niveles[i],self.pantalla, self.monedas))
                        self.niveles_juegos.append(Nivel(self.niveles[i],self.pantalla, self.monedas))
                    Main()
                elif self.numeroNivelActual != 3: """
                self.nivelActual =self.niveles_juegos[self.numeroNivelActual]
                self.nivelActual.monedas=self.monedas
                

            pygame.display.update()
            self.reloj.tick(30)



Main()