from csv import reader
from settings import TAMANIO_LOSA
from os import walk
import pygame


def import_folder(path):
    surface_list = []
    for _, __, image_files in walk(path):
        for image in image_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list



def importar_csv_plantilla(path):
    mapa_terreno = []
    with open(path) as map:
        nivel = reader(map, delimiter=',')
        for row in nivel:
            mapa_terreno.append(list(row))
        return mapa_terreno


def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / TAMANIO_LOSA)
    tile_num_y = int(surface.get_size()[1] / TAMANIO_LOSA)

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * TAMANIO_LOSA
            y = row * TAMANIO_LOSA
            new_surf = pygame.Surface((TAMANIO_LOSA, TAMANIO_LOSA), flags= pygame.SRCALPHA)
            new_surf.blit(surface, (0, 0), pygame.Rect(x,y,TAMANIO_LOSA,TAMANIO_LOSA))
            cut_tiles.append(new_surf)

    return cut_tiles
