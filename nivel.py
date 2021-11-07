import pygame
from settings import TAMANIO_LOSA,AMPLIACION_ESCALA
from soporte import import_cut_graphics, importar_csv_plantilla
from tile import StaticTile, Tile

class Nivel:
    def __init__(self, nivel_data, superficie):
        self.display_superficie = superficie
        self.desplazamiento_mundo = 0

        capa_terreno = importar_csv_plantilla(nivel_data['terreno'])
        self.terreno_sprites = self.crear_grupo_sprites(capa_terreno,"terreno")

    def crear_grupo_sprites(self,layout,tipo):
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

                    ''' if tipo == 'terrain':
    						terrain_tile_list = import_cut_graphics('../graphics/terrain/terrain_tiles.png')
						tile_surface = terrain_tile_list[int(val)]
						sprite = StaticTile(tile_size,x,y,tile_surface)
 '''
        return grupo_sprites


    def run(self):
        self.terreno_sprites.draw(self.display_superficie)
        self.terreno_sprites.update(self.desplazamiento_mundo)
    
    def move(self,x):
        self.terreno_sprites.update(x)