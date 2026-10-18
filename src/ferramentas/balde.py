from .ferramenta import Ferramenta
from utils.algoritmos import flood_fill

class Balde(Ferramenta):
    def __init__(self, canvas, cor_atual):
        self.canvas = canvas
        self.cor = cor_atual
        self.ponto_anterior = None
        self.rasterizada = []

    def clicar_esquerdo(self, mouse_x, mouse_y):
        self.ponto_final = None
        self.rasterizada = flood_fill(self.canvas, mouse_x, mouse_y, self.cor)
        

    def arrastar_esquerdo(self, mouse_x, mouse_y):
         pass

    def soltar_esquerdo(self, mouse_x, mouse_y):
        pass

    def clicar_direito(self, mouse_x, mouse_y):
        self.rasterizada = []
        self.ponto_anterior = None

    def arrastar_direito(self, mouse_x, mouse_y):
        pass

    def soltar_direito(self, mouse_x, mouse_y):
        pass

    def desenhar_previa(self):
        pass