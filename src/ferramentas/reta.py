from .ferramenta import Ferramenta
from utils.algoritmos import calcular_linha

class Reta(Ferramenta):
    def __init__(self, canvas, cor_atual):
        self.canvas = canvas
        self.cor = cor_atual
        self.ponto_inicial = None
        self.ponto_final = None
        self.rasterizada = [] # armazena todos os pontos da linha desenhada

    def clicar_esquerdo(self, mouse_x, mouse_y):
        self.ponto_inicial = (mouse_x, mouse_y)
        self.ponto_final = None
        self.rasterizada = []

    def arrastar_esquerdo(self, mouse_x, mouse_y):
        self.ponto_final = (mouse_x, mouse_y)

        # se tem os 2 pontos da linha salvos
        if self.ponto_inicial and self.ponto_final:
            self.rasterizada = calcular_linha(self.ponto_inicial[0], self.ponto_inicial[1], self.ponto_final[0], self.ponto_final[1])
            
    def soltar_esquerdo(self, mouse_x, mouse_y):
        # se tem os 2 pontos da linha salvos
        if self.ponto_inicial and self.ponto_final:
                self.rasterizada = calcular_linha(self.ponto_inicial[0], self.ponto_inicial[1], self.ponto_final[0], self.ponto_final[1])

        # salva a linha na matriz do canvas
        for ponto in self.rasterizada:
            self.canvas.put_pixel(ponto[0], ponto[1], self.cor)

        self.ponto_inicial = None
        self.ponto_final = None
        self.rasterizada = [] # apaga a previa da linha

    def clicar_direito(self, mouse_x, mouse_y):
        self.ponto_inicial = None
        self.ponto_final = None
        self.rasterizada = []

    def arrastar_direito(self, mouse_x, mouse_y):
        pass

    def soltar_direito(self, mouse_x, mouse_y):
        pass

    def desenhar_previa(self):
        if self.rasterizada: # se temos uma previa da linha
            self.canvas.desenhar_pixels(self.rasterizada, self.cor) # desenha a linha (sem salvar na matriz do canvas)

