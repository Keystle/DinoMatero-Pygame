import pygame
from settings import TAMANIO_LOSA, AMPLIACION_ESCALA,PANTALLA_ALTO,PANTALLA_ANCHO
from soporte import import_cut_graphics, importar_csv_plantilla
from tile import *
from jugador import Jugador
from decoracion import Cielo

class Nivel:
    def __init__(self, nivel_data, superficie):
#INSTANCIAMOS JUGADOR
        self.personaje = Jugador(200, 687, 64, 44)

        #self.personaje = pygame.sprite.GroupSingle()

        self.display_superficie = superficie
        self.desplazamiento_mundo = 0

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
                        sprite = Coin(TAMANIO_LOSA,x,y,'./images/items/Gold_Coin')
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

    
    """ def colision_horizontal(self): 
        personaje = self.personaje.sprite
        personaje.rect.x += personaje.direction.x * personaje.vel
        self.personaje.get_rect()
    
    def scroll_horizontal(self):
        personaje = self.personaje.sprite
        personaje_x = personaje.rect.centerx
        direccion_x = personaje.direccion.x

        if personaje_x < PANTALLA_ANCHO / 4 and direccion_x < 0:
            self.desplazamiento_mundo = 8
            personaje.vel = 0
        elif personaje_x > PANTALLA_ANCHO - (PANTALLA_ANCHO / 4) and direccion_x > 0:
            self.desplazamiento_mundo.vel = -8
            personaje.vel = 0
        else:
            self.desplazamiento_mundo = 0
            personaje.vel = 8
		 """


    def run(self,keys):
        #MOVIMIENTO DEL PERSONAJE
        self.desplazamiento_mundo = self.personaje.move(keys)


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

        #self.scroll_horizontal()

        #UPDATE JUGADOR
        self.personaje.draw(self.display_superficie)

        #self.colision_horizontal()

        
        
    
    