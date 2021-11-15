import pygame
from settings import *
from soporte import import_folder
class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # SONIDOS
        self.salto_sonido = pygame.mixer.Sound("audio/effects/jump.wav")
        
        self.salto_sonido.set_volume(0.5)
        # MOVIMIENTO
        self.vel = 10
        self.gravedad=1.8
        self.vel_salto=-28
        
        # ANIMACIONES
        self.importar_imagenes_personaje()
        self.indice_frame = 0
        self.animacion_vel = 0.15
        self.status = "quieto"
        self.mirando_izquierda = False   
        # Alineamiento de la hitbox
        self.sobre_el_suelo=False
        self.sobre_el_techo=False
        self.sobre_izquierda=False
        self.sobre_derecha = False

        # SPRITE DEL PERSONAJE
        #  Y COLISION
        self.image = self.animaciones["quieto"][self.indice_frame]
        self.rect = self.image.get_rect(topleft=pos)

        self.direccion = pygame.Vector2(0,0)
        
    # ANIMACIONES
    def importar_imagenes_personaje(self):
        carpeta_ubicacion = "images/personaje/"
        self.animaciones = {"quieto":[],"run":[],"salto":[]}
        for animacion in self.animaciones.keys():
            full_path = carpeta_ubicacion + animacion
            self.animaciones[animacion] = import_folder(full_path)

    def get_status(self):
        if self.direccion.y < 0 or self.direccion.y > 0:
            self.status="salto"
        else:
            if self.direccion.x != 0:
                self.status = "run"
            else:
                self.status = "quieto"
        
    def animate(self):
        animacion = self.animaciones[self.status]

        self.indice_frame += self.animacion_vel
        if self.indice_frame >= len(animacion):
            self.indice_frame = 0

        image = animacion[int(self.indice_frame)]
        # VOLTEAR LA IMAGEN
        if self.mirando_izquierda:
            imagen_volteada = pygame.transform.flip(image,True,False)
            self.image = imagen_volteada
        else:
            self.image = image

        # CORRECCIONES A LA HITBOX Y ALINEAMIENTO

        if self.sobre_el_suelo and self.sobre_derecha:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.sobre_el_suelo and self.sobre_izquierda:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.sobre_el_suelo:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.sobre_el_techo and self.sobre_derecha:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.sobre_el_techo and self.sobre_izquierda:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.sobre_el_techo:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def movimiento(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direccion.x=1
            self.mirando_izquierda = False
        
        elif keys[pygame.K_d]:
            self.direccion.x=1
            self.mirando_izquierda = False

        elif keys[pygame.K_LEFT]:
            self.direccion.x=-1
            self.mirando_izquierda = True
        
        elif keys[pygame.K_a]:
            self.direccion.x=-1
            self.mirando_izquierda = True

        else:
            self.direccion.x=0
        if keys[pygame.K_SPACE] and self.sobre_el_suelo:
            self.saltar()
            self.salto_sonido.play()

 
    #def draw(self, pantalla):
        # if self.conteoCaminata + 1 >= 5:
        #     self.conteoCaminata = 0
        # if self.izquierda:
        #     pantalla.blit(
        #         self.caminarIzquierda[self.conteoCaminata // 1], (int(self.x),int(self.y)))
        #     self.conteoCaminata += 1
        # elif self.derecha:
        #     pantalla.blit(
        #         self.caminarDerecha[self.conteoCaminata // 1], (int(self.x),int(self.y)))
        #     self.conteoCaminata += 1
        # elif self.salto:
        #     pantalla.blit(
        #         self.salta[self.conteoCaminata // 1], (int(self.x),int(self.y)))
        #     self.conteoCaminata += 1
        # else:
        #     pantalla.blit(self.quieto, (int(self.x),int(self.y)))
        # pantalla.blit()
       
    def aplicar_gravedad(self):
        self.direccion.y += self.gravedad
        self.rect.y += self.direccion.y
    
    def saltar(self):
        self.direccion.y = self.vel_salto
       
    def update(self):
        self.movimiento()
        self.get_status()
        self.animate()