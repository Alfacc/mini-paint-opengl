from .ferramenta import Ferramenta
from utils.algoritmos import calcular_linha

class Pincel(Ferramenta):
    def __init__(self, canvas, cor_atual):
        self.canvas = canvas
        self.cor = cor_atual
        self.ponto_anterior = None
        self.rasterizada = []

    def clicar_esquerdo(self, mouse_x, mouse_y):
        self.rasterizada = []
        self.rasterizada.append((mouse_x, mouse_y))
        self.ponto_anterior = (mouse_x, mouse_y)

    def arrastar_esquerdo(self, mouse_x, mouse_y):
        # array com os pontos ja pintados antes, e a os pontos entre o ultimo ponto captado e o ponto atual (uma linha)
        if self.ponto_anterior:
            # list set para apagar as duplicatas do array (caso passe o pincel em cima de onde ja foi pintado)
            self.rasterizada = list(set(self.rasterizada + calcular_linha(self.ponto_anterior[0], self.ponto_anterior[1], mouse_x, mouse_y)))

        self.ponto_anterior = (mouse_x, mouse_y)

    def soltar_esquerdo(self, mouse_x, mouse_y):
        for ponto in self.rasterizada:
            self.canvas.put_pixel(ponto[0], ponto[1], self.cor)

        self.rasterizada = []
        self.ponto_anterior = None

    def clicar_direito(self, mouse_x, mouse_y):
        self.rasterizada = []
        self.ponto_anterior = None

    def arrastar_direito(self, mouse_x, mouse_y):
        pass

    def soltar_direito(self, mouse_x, mouse_y):
        pass

    def desenhar_previa(self):
        if self.rasterizada: # se temos uma previa dos pixels pintados
            self.canvas.desenhar_pixels(self.rasterizada, self.cor) # desenha os pixels pintados (sem salvar na matriz do canvas)