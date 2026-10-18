from .ferramenta import Ferramenta
from utils.algoritmos import circulo_cheio

class CirculoCheio(Ferramenta):
    def __init__(self, canvas, cor_atual):
      self.canvas = canvas
      self.cor = cor_atual
      self.ponto_inicial = None
      self.ponto_final = None
      self.raio = None
      self.rasterizada = [] # armazena todos os pontos da linha desenhada

    def clicar_esquerdo(self, mouse_x, mouse_y):
        self.ponto_inicial = (mouse_x, mouse_y)
        self.ponto_final = None
        self.rasterizada = []

    def arrastar_esquerdo(self, mouse_x, mouse_y):
        self.ponto_final = (mouse_x, mouse_y)

        # A partir do ponto inicial calcula dinamicamente o tamanho do círculo
        dx = self.ponto_final[0] - self.ponto_inicial[0]
        dy = self.ponto_final[1] - self.ponto_inicial[1]
        self.raio =  int((dx**2 + dy**2) ** 0.5)

        if self.ponto_inicial and self.ponto_final:
            self.rasterizada = circulo_cheio(self.ponto_inicial[0], self.ponto_inicial[1], self.raio)
            
    def soltar_esquerdo(self, mouse_x, mouse_y):
        # salva a linha na matriz do canvas
        for ponto in self.rasterizada:
            self.canvas.put_pixel(ponto[0], ponto[1], self.cor, usar_espessura=False)

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
        if self.rasterizada: # se temos uma previa do ponto
            self.canvas.desenhar_pixels(self.rasterizada, self.cor, usar_espessura=False) # desenha o círculo (sem salvar na matriz do canvas)

    