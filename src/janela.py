import glfw
from OpenGL.GL import *

class Janela:
    def __init__(self, largura, altura, titulo):
        self.largura = largura
        self.altura = altura
        self.titulo = titulo
        self.referencia = None

    def inicializar(self):
        if not glfw.init(): # erro ao iniciar o GLFW
            return 1

        self.referencia = glfw.create_window(self.largura, self.altura, self.titulo, None, None)
        if not self.referencia: # erro ao criar janela
            glfw.terminate()
            return 2

        glfw.make_context_current(self.referencia) # vira o novo contexto grafico
        return 0

    def encerrar(self):
        glfw.terminate()

    def esta_aberta(self): #
        return not glfw.window_should_close(self.referencia) # 

    def atualizar_tela(self): # troca os buffers para atualizar a imagem da janela
        glfw.swap_buffers(self.referencia)

    def processar_eventos(self): # captura os eventos/acoes do usuario
        glfw.poll_events()
