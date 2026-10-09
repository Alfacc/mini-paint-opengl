import glfw
from OpenGL.GL import *
import imgui

from core.janela import Janela
from core.canvas import Canvas
from constantes import *
from ferramentas import Pincel

def main():
    def callback_botao_mouse(janela, botao, acao, mods):
        x, y = glfw.get_cursor_pos(janela)
        x, y = int(x), int(y)

        if botao == glfw.MOUSE_BUTTON_LEFT:
            if acao == glfw.PRESS:
                ferramenta_atual.clicar_esquerdo(x, y)
            elif acao == glfw.RELEASE:
                ferramenta_atual.soltar_esquerdo(x, y)
                
        elif botao == glfw.MOUSE_BUTTON_RIGHT:
            if acao == glfw.PRESS:
                ferramenta_atual.clicar_direito(x, y)
            elif acao == glfw.RELEASE:
                ferramenta_atual.soltar_direito(x, y)

    def callback_movimento_mouse(janela, pos_x, pos_y):
        x, y = int(pos_x), int(pos_y)
        #print(f"Posicao: {x}, {y}")

        # Se o botão esquerdo está pressionado enquanto o mouse se move
        estado_esquerdo = glfw.get_mouse_button(janela, glfw.MOUSE_BUTTON_LEFT)
        if estado_esquerdo == glfw.PRESS:
            ferramenta_atual.arrastar_esquerdo(x, y)
            
        # Se o botão direito está pressionado enquanto o mouse se move
        estado_direito = glfw.get_mouse_button(janela, glfw.MOUSE_BUTTON_RIGHT)
        if estado_direito == glfw.PRESS:
            ferramenta_atual.arrastar_direito(x, y)


    # PROGRAMA

    print("Iniciando programa...")

    janela = Janela(1200, 900, "Mini Paint", COR_FUNDO_JANELA)

    estado = janela.inicializar()
    if estado == 1:
        print("Não foi possível inicializar o GLFW.")
    elif estado == 2:
        print("Erro ao criar janela.")
    else:
         print("Janela criada com sucesso.")

    glfw.set_mouse_button_callback(janela.referencia, callback_botao_mouse)
    glfw.set_cursor_pos_callback(janela.referencia, callback_movimento_mouse)

    canvas = Canvas(800, 600, COR_FUNDO_CANVAS, (janela.largura, janela.altura))

    cor_primaria = (0, 0, 0) #preto
    modo_atual = ModoFerramenta.PINCEL

    ferramentas_disponiveis = {
        ModoFerramenta.PINCEL: Pincel(canvas, cor_primaria)
    }
    ferramenta_atual = ferramentas_disponiveis[modo_atual]

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
