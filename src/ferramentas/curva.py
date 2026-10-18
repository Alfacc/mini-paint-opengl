from .ferramenta import Ferramenta
from utils.algoritmos import calcular_linha, calcular_curva

class Curva(Ferramenta):
    def __init__(self, canvas, cor_atual):
        self.canvas = canvas
        self.cor = cor_atual
        self.p0 = None # Ponto inicial
        self.p1 = None # Ponto de controle (que puxa a curva)
        self.p2 = None # Ponto final
        self.etapa = 0 # 0 = definindo a linha base (p0 -> p2), 1 = curvando (p1)
        self.rasterizada = []

    def clicar_esquerdo(self, mouse_x, mouse_y):
        if self.etapa == 0:
            self.p0 = (mouse_x, mouse_y)
            self.p2 = (mouse_x, mouse_y)
            self.rasterizada = []
        elif self.etapa == 1:
            # No segundo clique, o mouse já puxa a curva
            self.p1 = (mouse_x, mouse_y)
            self.rasterizada = calcular_curva(self.p0, self.p1, self.p2)

    def arrastar_esquerdo(self, mouse_x, mouse_y):
        if self.etapa == 0 and self.p0:
            self.p2 = (mouse_x, mouse_y)
            self.rasterizada = calcular_linha(self.p0[0], self.p0[1], self.p2[0], self.p2[1])
        elif self.etapa == 1 and self.p0 and self.p2:
            self.p1 = (mouse_x, mouse_y)
            self.rasterizada = calcular_curva(self.p0, self.p1, self.p2)

    def soltar_esquerdo(self, mouse_x, mouse_y):
        if self.etapa == 0 and self.p0 and self.p2:
            # Terminou de traçar a linha base; agora vai para a etapa 1 (curvar)
            self.etapa = 1
        elif self.etapa == 1:
            # Terminou de curvar: salva os pixels no canvas e reseta para a próxima curva
            for ponto in self.rasterizada:
                self.canvas.put_pixel(ponto[0], ponto[1], self.cor)
            self.resetar()

    def clicar_direito(self, mouse_x, mouse_y):
        # Botão direito cancela o desenho da curva atual
        self.resetar()

    def arrastar_direito(self, mouse_x, mouse_y):
        pass

    def soltar_direito(self, mouse_x, mouse_y):
        pass

    def desenhar_previa(self):
        if self.rasterizada:
            self.canvas.desenhar_pixels(self.rasterizada, self.cor)

    def resetar(self):
        self.p0 = None
        self.p1 = None
        self.p2 = None
        self.etapa = 0
        self.rasterizada = []