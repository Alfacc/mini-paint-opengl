from .ferramenta import Ferramenta
#from core.canvas import Canvas

class Pincel(Ferramenta):
    def __init__(self, canvas, cor_atual):
        self.canvas = canvas
        self.cor = cor_atual

    def clicar_esquerdo(self, mouse_x, mouse_y):
        self.canvas.put_pixel(mouse_x, mouse_y, self.cor)

    def arrastar_esquerdo(self, mouse_x, mouse_y):
        self.canvas.put_pixel(mouse_x, mouse_y, self.cor)

    def soltar_esquerdo(self, mouse_x, mouse_y):
        pass

    def clicar_direito(self):
        pass

    def arrastar_direito(self):
        pass

    def soltar_direito(self):
        pass