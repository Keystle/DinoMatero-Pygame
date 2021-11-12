import pygame
from settings import *
import time
from decoracion import *
import keyboard
pygame.init()

########### $$$$CONSTANTES$$$$ ###########
#Colores
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
GREEN   = (85, 255, 51)
RED     = (228, 22, 59 )
BLUE    = (24, 26, 82 )

#Ventana
pantalla = pygame.display.set_mode((PANTALLA_ANCHO,PANTALLA_ALTO))
cielo = pygame.image.load('./images/background/fondoUnico.png').convert()
cielo = pygame.transform.scale(cielo, (PANTALLA_ANCHO, PANTALLA_ALTO))


#Fuente
font = pygame.font.SysFont("Source Serif Pro Black", 50)

############### MENU INICIO ###############################
def mensaje_en_pantalla(msg, color, txt_x, txt_y):
    txt_pantalla = font.render(msg, True, color)
    pantalla.blit(txt_pantalla, (txt_x, txt_y))

def menu():
    #cielo.draw(self.display_superficie,self.desplazamiento_mundo)
    pantalla.blit(cielo,(0, 0))
    mensaje_en_pantalla("JAMPING", RED, 150, 110)
    mensaje_en_pantalla("1. Jugar", WHITE, 180, 200)
    mensaje_en_pantalla("2. Instrucciones", WHITE, 180, 250)
    mensaje_en_pantalla("3. Salir", WHITE, 180, 300)
    pygame.display.update()

def instrucciones():
    pantalla.fill(GREEN)
    mensaje_en_pantalla("Use las flachas izquierda y ", WHITE, 20, 220)
    mensaje_en_pantalla("derecha o A y D para moverse, ", WHITE, 20, 270)
    mensaje_en_pantalla("para saltar use la tecla SPACE", WHITE, 20, 320)
    mensaje_en_pantalla("", WHITE, 20, 370)
    mensaje_en_pantalla("", WHITE, 20, 420)
    pygame.display.update()
  
    time.sleep(5)


##################################################


############################################################


''' 
fin_bucle = False   
while not fin_bucle:
    menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                fin_bucle = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                print("hola mundo")
            if event.key == pygame.K_2:
                instrucciones()
            
            if event.key == pygame.K_3:
                pygame.display.quit()
                fin_bucle = True
                    
                    
                       
pygame.display.quit() '''