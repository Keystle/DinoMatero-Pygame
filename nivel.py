import pygame

class Nivel:
    def __init__(self, nivel_data, superficie):
        self.display_superficie = superficie

        capa_terreno = import_csv_layout(nivel_data['terreno'])

    def run(self):
        pass
    