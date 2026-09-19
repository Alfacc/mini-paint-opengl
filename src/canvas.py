from OpenGL.GL import *
import numpy as np

# Arquivo para gerenciar qualquer operação no canvas (desenhar pixels, pegar pixels, limpar canvas)

class Canvas:
    def __init__(self, largura, altura, cor_fundo, formato_janela):
        self.largura = largura
        self.altura = altura
        self.cor_fundo = cor_fundo
        self.formato_janela = formato_janela
        self.topo_esquerdo = self.encontrar_topo_esquerdo()
        self.matriz_pixels = self.limpar()

    # o OpenGL desenha toda a matriz_pixels comecando do topo_esquerdo
    def desenhar(self):
        # posicao onde OpenGL usara glDrawPixels
        glWindowPos2i(self.topo_esquerdo[0], self.formato_janela[1] - self.topo_esquerdo[1])

        # inversao do eixo y que o OpenGL desenhara a matriz, pois o eixo y do OpenGL é invertido (vai de baixo pra cima)
        glPixelZoom(1.0, -1.0)

        glDrawPixels(self.largura, self.altura, GL_RGB, GL_UNSIGNED_BYTE, self.matriz_pixels)

    # limpa a matriz_pixels (fica da cor_fundo)
    def limpar(self):
        return np.zeros((self.altura, self.largura, 3), dtype=np.uint8) + self.cor_fundo

    # retorna a cor do pixel numa posicao do canva
    def get_pixel(self, x, y):
        if self.esta_dentro(x, y):
            return self.matriz_pixels[y][x]
        return None

    # muda a cor de um pixel numa posicao do canva
    def put_pixel(self, x, y, cor):
        if self.esta_dentro(x, y):
            self.matriz_pixels[y][x] = cor

    # verifica se o mouse esta dentro do canvas
    def esta_dentro(self, mouse_x, mouse_y):
        inicio_x = self.topo_esquerdo[0]
        fim_x = inicio_x + self.largura

        inicio_y = self.topo_esquerdo[1]
        fim_y = inicio_y + self.altura

        if inicio_x < mouse_x < fim_x and inicio_y < mouse_y < fim_y:
            return True
        return False

    # encontra posicao do topo esquerdo para centralizar a janela
    def encontrar_topo_esquerdo(self):
        x = (self.formato_janela[0] - self.largura) // 2
        y = (self.formato_janela[1] - self.altura) // 2
        return (x,y)
