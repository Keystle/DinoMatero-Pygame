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

        self.display_superficie = superficie
        self.desplazamiento_mundo = 0

        capa_terreno = importar_csv_plantilla(nivel_data['terreno'])
        self.terreno_sprites = self.crear_grupo_sprites(
            capa_terreno, "terreno")

        capa_moneda = importar_csv_plantilla(nivel_data['moneda'])
        self.moneda_sprites = self.crear_grupo_sprites(capa_moneda, "moneda")

        capa_arbol = importar_csv_plantilla(nivel_data['arbol'])
        self.arbol_sprites = self.crear_grupo_sprites(capa_arbol, "arbol")

        capa_arbusto = importar_csv_plantilla(nivel_data['arbusto'])
        self.arbusto_sprites = self.crear_grupo_sprites(
            capa_arbusto, "arbusto")

        capa_cueva = importar_csv_plantilla(nivel_data['cueva'])
        self.cueva_sprites = self.crear_grupo_sprites(capa_cueva, "cueva")

        capa_muro = importar_csv_plantilla(nivel_data['muro'])
        self.muro_sprites = self.crear_grupo_sprites(capa_muro, "muro")

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

                    ''' if tipo == 'muro':
                        lista_losa_muro = import_cut_graphics('./images/background/Tileset64.png')
                        superficie_losa = lista_losa_muro[int(val)]
                        sprite = StaticTile(TAMANIO_LOSA, x, y, superficie_losa)
                        grupo_sprites.add(sprite) '''


        return grupo_sprites

    

    
			

    def run(self,keys):
        #MOVIMIENTO DEL PERSONAJE
        self.desplazamiento_mundo = self.personaje.move(keys)


#         DECORACION
        self.cielo.draw(self.display_superficie,self.desplazamiento_mundo)

        self.arbol_sprites.draw(self.display_superficie)
        self.arbol_sprites.update(self.desplazamiento_mundo)

        ''' self.muro_sprites.update(self.desplazamiento_mundo)
        self.muro_sprites.draw(self.display_superficie) '''

        self.arbusto_sprites.draw(self.display_superficie)
        self.arbusto_sprites.update(self.desplazamiento_mundo)

        self.terreno_sprites.draw(self.display_superficie)
        self.terreno_sprites.update(self.desplazamiento_mundo)

        self.cueva_sprites.draw(self.display_superficie)
        self.cueva_sprites.update(self.desplazamiento_mundo)

        self.moneda_sprites.draw(self.display_superficie)
        self.moneda_sprites.update(self.desplazamiento_mundo)

        #UPDATE JUGADOR
        self.personaje.draw(self.display_superficie)

        
        
    
    