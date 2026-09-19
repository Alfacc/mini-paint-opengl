import glfw
from OpenGL.GL import *

from janela import Janela
from canvas import Canvas

def main():
    cor_fundo_janela = (128, 128, 128) # cinza
    cor_fundo_canvas = (255, 255, 255) # branco

    print("Iniciando programa...")

    janela = Janela(1200, 900, "Mini Paint", cor_fundo_janela)

    estado = janela.inicializar()
    if estado == 1:
        print("Não foi possível inicializar o GLFW.")
    elif estado == 2:
        print("Erro ao criar janela.")
    else:
         print("Janela criada com sucesso.")

    canvas = Canvas(800, 600, cor_fundo_canvas, (janela.largura, janela.altura))
    
    # LOOP PRINCIPAL
    while janela.esta_aberta():
        glClear(GL_COLOR_BUFFER_BIT) # poe os pixels da janela com a cor de fundo definida
        

        canvas.desenhar()

        janela.atualizar_imagem()
        janela.capturar_eventos()
    
    janela.encerrar() # fim do programa

    print("Encerrando programa...")

if __name__ == "__main__":
    main()