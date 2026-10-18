from OpenGL.GL import *
import glfw
import numpy as np

# Arquivo para gerenciar qualquer operação no canvas (desenhar pixels, pegar pixels, limpar canvas)

class Canvas:
    def __init__(self, largura, altura, cor_fundo, formato_janela, espessura=1):
        self.largura = largura
        self.altura = altura
        self.cor_fundo = cor_fundo
        self.formato_janela = formato_janela
        self.espessura = espessura # (1, 3 ou 5)
        self.topo_esquerdo = self.encontrar_topo_esquerdo()
        self.matriz_pixels = np.zeros((self.altura, self.largura, 3), dtype=np.uint8) + self.cor_fundo # canvas da cor de fundo

    # o OpenGL desenha toda a matriz_pixels comecando do topo_esquerdo
    def desenhar(self):
        # posicao onde OpenGL usara glDrawPixels
        glWindowPos2i(self.topo_esquerdo[0], self.formato_janela[1] - self.topo_esquerdo[1])

        # inversao do eixo y que o OpenGL desenhara a matriz, pois o eixo y do OpenGL é invertido (vai de baixo pra cima)
        glPixelZoom(1.0, -1.0)

        # desenha toda a matriz de uma vez na tela
        glDrawPixels(self.largura, self.altura, GL_RGB, GL_UNSIGNED_BYTE, self.matriz_pixels)

    # limpa a matriz_pixels (fica da cor_fundo)
    def limpar(self):
        self.matriz_pixels = np.zeros((self.altura, self.largura, 3), dtype=np.uint8) + self.cor_fundo

    # retorna a cor do pixel numa posicao do canva
    def get_pixel(self, mouse_x, mouse_y):
        if self.esta_dentro(mouse_x, mouse_y):
            x, y = self.corrigir_mouse(mouse_x, mouse_y)
            return self.matriz_pixels[y][x]
        return None

    # muda a cor de um pixel numa posicao do canva
    def put_pixel(self, mouse_x, mouse_y, cor, usar_espessura=True):
        raio = (self.espessura // 2) if usar_espessura else 0

        for dy in range(-raio, raio + 1):
            for dx in range(-raio, raio + 1):
                px, py = mouse_x + dx, mouse_y + dy
                if self.esta_dentro(px, py):
                    x, y = self.corrigir_mouse(px, py)
                    self.matriz_pixels[y][x] = cor

    # muda a cor de pixels sem armazenar no canva
    def desenhar_pixels(self, pontos, cor, usar_espessura=True):
        #Aceita de 0 a 255, não precisa fazer cor[0]/cor[255] etc.
        glColor3ub(*cor)
        glPointSize(float(self.espessura if usar_espessura else 1))
        glBegin(GL_POINTS)

        for ponto in pontos:
            mouse_x, mouse_y = ponto
            if self.esta_dentro(mouse_x, mouse_y):
                glVertex2f(mouse_x + 0.5, mouse_y + 0.5)

        glEnd()
            
    # verifica se o mouse esta dentro do canvas
    def esta_dentro(self, mouse_x, mouse_y):
        inicio_x = self.topo_esquerdo[0]
        fim_x = inicio_x + self.largura

        inicio_y = self.topo_esquerdo[1]
        fim_y = inicio_y + self.altura

        if inicio_x <= mouse_x < fim_x and inicio_y <= mouse_y < fim_y:
            return True
        return False

    # encontra posicao do topo esquerdo para centralizar a janela
    def encontrar_topo_esquerdo(self):
        x = (self.formato_janela[0] - self.largura) // 2
        y = (self.formato_janela[1] - self.altura) // 2
        return (x,y)

    def corrigir_mouse(self, mouse_x, mouse_y):
        canvas_x = mouse_x - self.topo_esquerdo[0]
        canvas_y = mouse_y - self.topo_esquerdo[1]

        return canvas_x, canvas_y
