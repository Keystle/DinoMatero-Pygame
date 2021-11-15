import pygame
from pygame.draw import rect
from settings import TAMANIO_LOSA, AMPLIACION_ESCALA,PANTALLA_ALTO,PANTALLA_ANCHO
from soporte import import_cut_graphics, importar_csv_plantilla
from tile import *
from jugador import Jugador
from decoracion import Cielo


class Nivel:
    def __init__(self, nivel_data, superficie, monedaJuego):
        # INSTANCIAR MONEDA


#INSTANCIAMOS JUGADOR
        #self.personaje = Jugador(200, 687, 64, 44)

        # FUENTE PARA CONTADOR DE MUERTES

        self.font = pygame.font.SysFont("Arial", 32)

        # SONIDOS
        self.coin_sonido = pygame.mixer.Sound("audio/effects/coin.wav")
        self.coin_sonido.set_volume(0.5)

        self.jugadorSprite = pygame.sprite.GroupSingle()
        self.jugador = Jugador((500,0))
        self.jugadorSprite.add(self.jugador)

        self.display_superficie = superficie
        self.x_actual=0
        self.desplazamiento_mundo = 0

        self.suma_desplazada = 0

        self.monedas = monedaJuego
        self.contador_muertes = 0
        self.finNivel = False

        capa_terreno = importar_csv_plantilla(nivel_data['terreno'])
        self.terreno_sprites = self.crear_grupo_sprites(
            capa_terreno, "terreno")

        capa_moneda = importar_csv_plantilla(nivel_data['moneda'])
        self.moneda_sprites = self.crear_grupo_sprites(capa_moneda, "moneda")

        capa_arbol = importar_csv_plantilla(nivel_data['arbol'])
        self.arbol_sprites = self.crear_grupo_sprites(capa_arbol, "arbol")

        capa_arbol2 = importar_csv_plantilla(nivel_data['arbol2'])
        self.arbol2_sprites = self.crear_grupo_sprites(capa_arbol2, "arbol2")

        capa_arbusto = importar_csv_plantilla(nivel_data['arbusto'])
        self.arbusto_sprites = self.crear_grupo_sprites(
            capa_arbusto, "arbusto")

        capa_cueva = importar_csv_plantilla(nivel_data['cueva'])
        self.cueva_sprites = self.crear_grupo_sprites(capa_cueva, "cueva")

        capa_muro = importar_csv_plantilla(nivel_data['muro'])
        self.muro_sprites = self.crear_grupo_sprites(capa_muro, "muro")
        
        capa_muro2 = importar_csv_plantilla(nivel_data['muro2'])
        self.muro2_sprites = self.crear_grupo_sprites(capa_muro2, "muro2")

        #decoracion
        self.cielo = Cielo(8)

    """ def change_coins(self,amount):
    		self.coins += amount """

    def crear_grupo_sprites(self, layout, tipo):
        grupo_sprites = pygame.sprite.Group()

        for fila_indice, fila in enumerate(layout):
            for columna_indice, val in enumerate(fila):
                if val != '-1':
                    x = columna_indice * TAMANIO_LOSA
                    y = fila_indice * TAMANIO_LOSA

                    if tipo == 'terreno':
                        lista_losa_terreno = import_cut_graphics('./images/background/Tileset64.png')
                        superficie_losa = lista_losa_terreno[int(val)]
                        sprite = StaticTile(TAMANIO_LOSA, x, y, superficie_losa)
                        grupo_sprites.add(sprite)


                    if tipo == 'moneda':
                        sprite = Coin(TAMANIO_LOSA,x,y,'./images/items/Gold_Coin',50)
                        grupo_sprites.add(sprite)

                    if tipo == 'arbol':
                        lista_losa_arbol = import_cut_graphics('./images/background/Decors64.png')
                        superficie_losa = lista_losa_arbol[int(val)]
                        sprite = StaticTile(TAMANIO_LOSA, x, y, superficie_losa)
                        grupo_sprites.add(sprite)

                    if tipo == 'arbol2':
                        lista_losa_arbol2 = import_cut_graphics('./images/background/Decors64.png')
                        superficie_losa = lista_losa_arbol2[int(val)]
                        sprite = StaticTile(TAMANIO_LOSA, x, y, superficie_losa)
                        grupo_sprites.add(sprite)

                    if tipo == 'arbusto':
                        lista_losa_arbusto = import_cut_graphics('./images/background/Decors64.png')
                        superficie_losa = lista_losa_arbusto[int(val)]
                        sprite = StaticTile(TAMANIO_LOSA, x, y, superficie_losa)
                        grupo_sprites.add(sprite)

                    if tipo == 'cueva':
                        lista_losa_cueva = import_cut_graphics('./images/background/Tileset64.png')
                        superficie_losa = lista_losa_cueva[int(val)]
                        sprite = StaticTile(TAMANIO_LOSA, x, y, superficie_losa)
                        grupo_sprites.add(sprite)

                    if tipo == 'muro2':
                        lista_losa_muro2 = import_cut_graphics('./images/background/Tileset64.png')
                        superficie_losa = lista_losa_muro2[int(val)]
                        sprite = StaticTile(TAMANIO_LOSA, x, y, superficie_losa)
                        grupo_sprites.add(sprite)
                    
                    if tipo == 'muro':
                        lista_losa_muro = import_cut_graphics('./images/background/Decors64.png')
                        superficie_losa = lista_losa_muro[int(val)]
                        sprite = StaticTile(TAMANIO_LOSA, x, y, superficie_losa)
                        grupo_sprites.add(sprite)


        return grupo_sprites

    def desplazamiento_x(self):
        jugador = self.jugadorSprite.sprite
        jugador_x = jugador.rect.centerx
        direccion_x = self.jugador.direccion.x

        self.jugador.rect.x += self.jugador.direccion.x * self.jugador.vel
        
        if jugador_x < PANTALLA_ANCHO/4 and direccion_x < 0:
            self.desplazamiento_mundo=8
            self.suma_desplazada = self.suma_desplazada + self.desplazamiento_mundo
           
            self.jugador.vel=0
        elif jugador_x > PANTALLA_ANCHO - (PANTALLA_ANCHO/2) and direccion_x > 0:
            self.desplazamiento_mundo=-8
            self.suma_desplazada = self.suma_desplazada + self.desplazamiento_mundo
            
            self.jugador.vel=0
        else:
            self.desplazamiento_mundo=0
            self.jugador.vel=10

    def colision_horizontal(self): 
        jugador_sprite = self.jugadorSprite.sprite
        
    
        for sprite in self.terreno_sprites.sprites():
            if sprite.rect.colliderect(jugador_sprite.rect):
                if self.jugador.direccion.x < 0:
                    jugador_sprite.rect.left = sprite.rect.right
                    self.jugador.sobre_izquierda=True
                    self.x_actual = jugador_sprite.rect.left
                elif self.jugador.direccion.x > 0:
                    jugador_sprite.rect.right = sprite.rect.left
                    self.jugador.sobre_derecha=True
                    self.x_actual = jugador_sprite.rect.right

        if self.jugador.sobre_izquierda and (jugador_sprite.rect.left < self.x_actual or self.jugador.direccion.x >= 0):
            self.jugador.sobre_izquierda = False

        if self.jugador.sobre_derecha and (jugador_sprite.rect.right > self.x_actual or self.jugador.direccion.x <= 0):
            self.jugador.sobre_derecha = False
    
    def colision_vertical(self):
        jugador_sprite = self.jugadorSprite.sprite

        self.jugador.aplicar_gravedad()
        for sprite in self.terreno_sprites.sprites():
            if sprite.rect.colliderect(jugador_sprite.rect):
                if self.jugador.direccion.y > 0:
                    jugador_sprite.rect.bottom = sprite.rect.top
                    self.jugador.direccion.y=0
                    self.jugador.sobre_el_suelo = True
                elif self.jugador.direccion.y < 0:
                    jugador_sprite.rect.top = sprite.rect.bottom
                    self.jugador.direccion.y=0
                    self.jugador.sobre_el_techo = True

        if self.jugador.sobre_el_suelo and self.jugador.direccion.y<0 or self.jugador.direccion.y > 1:
            self.jugador.sobre_el_suelo=False
        if self.jugador.sobre_el_techo and self.jugador.direccion.y > 0:
            self.jugador.sobre_el_techo=False

    def colision_monedas(self):
        for monedita in self.moneda_sprites.sprites():
            if monedita.rect.colliderect(self.jugadorSprite.sprite.rect):
                self.monedas = self.monedas +1
                self.moneda_sprites.remove(monedita)
                self.coin_sonido.play()

    def colision_fin_nivel(self):
        for fin_nivel in self.cueva_sprites.sprites():
            if fin_nivel.rect.colliderect(self.jugadorSprite.sprite.rect):
                self.finNivel = True
        # colisionMoneda = pygame.sprite.spritecollide(self.jugadorSprite.sprite,self.moneda_sprites,True)
        # if colisionMoneda:
        #     for coin in colisionMoneda:
        #         self.change_coins(coin.value)
  
    def colision_perdida(self):
        if self.jugadorSprite.sprite.rect.y > PANTALLA_ALTO:
            self.restart_jugador()

    def restart_jugador(self):
        self.contador_muertes = self.contador_muertes +1
        self.desplazamiento_mundo= -self.suma_desplazada
        self.suma_desplazada = 0
        self.jugadorSprite.sprite.rect.y = 0
        self.jugadorSprite.sprite.rect.x = 500 
        
    def mostrar_muertes(self):
        texto = self.font.render(f"CONTADOR DE MUERTES: {self.contador_muertes}", 1, pygame.Color("black"))
        self.display_superficie.blit(texto,(10,30))

    def mostrar_monedas(self):
        texto = self.font.render(f"MONEDAS: {self.monedas}", 1, pygame.Color("yellow"))
        self.display_superficie.blit(texto,(10,60))
# fdefge
    def run(self):
        #MOVIMIENTO DEL PERSONAJE
        self.desplazamiento_x()
        self.colision_perdida()


#         DECORACION
        self.cielo.draw(self.display_superficie,self.desplazamiento_mundo)

        self.arbol2_sprites.draw(self.display_superficie)
        self.arbol2_sprites.update(self.desplazamiento_mundo)
        
        self.arbol_sprites.draw(self.display_superficie)
        self.arbol_sprites.update(self.desplazamiento_mundo)

        self.muro2_sprites.draw(self.display_superficie)
        self.muro2_sprites.update(self.desplazamiento_mundo)
        
        self.muro_sprites.draw(self.display_superficie)
        self.muro_sprites.update(self.desplazamiento_mundo)

        self.arbusto_sprites.draw(self.display_superficie)
        self.arbusto_sprites.update(self.desplazamiento_mundo)

        self.terreno_sprites.draw(self.display_superficie)
        self.terreno_sprites.update(self.desplazamiento_mundo)

        self.cueva_sprites.draw(self.display_superficie)
        self.cueva_sprites.update(self.desplazamiento_mundo)

        self.moneda_sprites.draw(self.display_superficie)
        self.moneda_sprites.update(self.desplazamiento_mundo)

        # TESTING
        # for sprite in self.terreno_sprites.sprites():
        #     pygame.draw.rect(self.display_superficie,(255, 0, 0), sprite,4 )
        # for sprite in self.moneda_sprites.sprites():
        #     pygame.draw.rect(self.display_superficie,(255, 0, 0), sprite,4 )
        # FIN TESTING

        #UPDATE JUGADOR
        self.colision_horizontal()
        self.colision_vertical()
        self.colision_monedas()
        self.colision_fin_nivel()
        self.mostrar_muertes()
        self.mostrar_monedas()
        self.jugadorSprite.draw(self.display_superficie)
        self.jugadorSprite.update()
    