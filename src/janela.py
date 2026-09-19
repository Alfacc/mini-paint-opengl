import glfw
from OpenGL.GL import *

# Arquivo para gerenciar tudo relacionado à janela do programa

class Janela:
    def __init__(self, largura, altura, titulo, cor_fundo):
        self.largura = largura
        self.altura = altura
        self.titulo = titulo
        self.cor_fundo = cor_fundo
        self.referencia = None

    # testa se o glfw e a janela foram criados corretamente, coloca a janela como contexto grafico e define a cor de fundo
    def inicializar(self):
        if not glfw.init(): # erro ao iniciar o GLFW
            return 1

        self.referencia = glfw.create_window(self.largura, self.altura, self.titulo, None, None)
        if not self.referencia: # erro ao criar janela
            glfw.terminate()
            return 2

        glfw.make_context_current(self.referencia) # vira o novo contexto grafico

        # define a cor de fundo da janela
        R = self.cor_fundo[0] / 255
        G = self.cor_fundo[1] / 255
        B = self.cor_fundo[2] / 255
        glClearColor(R, G, B, 1.0)

        return 0

    def encerrar(self):
        glfw.terminate()

    def atualizar_imagem(self):
        glfw.swap_buffers(self.referencia) # troca os buffers para atualizar a imagem da janela

    def capturar_eventos(self):
        glfw.poll_events() # captura os eventos/acoes do usuario

    def esta_aberta(self): #
        return not glfw.window_should_close(self.referencia)