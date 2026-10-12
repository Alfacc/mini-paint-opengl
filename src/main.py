import glfw
from OpenGL.GL import *
import imgui

from core.janela import Janela
from core.canvas import Canvas
from constantes import *
from ferramentas import Pincel, Linha

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

    # definicoes da projecao 2D do OpenGL
    glMatrixMode(GL_PROJECTION)
    glOrtho(0, janela.largura, janela.altura, 0, -1, 1) # tela vai do 0 ate a larg/alt. (0,0) esta no canto superior esq
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glfw.set_mouse_button_callback(janela.referencia, callback_botao_mouse)
    glfw.set_cursor_pos_callback(janela.referencia, callback_movimento_mouse)

    canvas = Canvas(800, 600, COR_FUNDO_CANVAS, (janela.largura, janela.altura))

    cor_primaria = (0, 0, 0) #preto

    modo_atual = ModoFerramenta.LINHA
    ferramentas_disponiveis = {
        ModoFerramenta.PINCEL: Pincel(canvas, cor_primaria),
        ModoFerramenta.LINHA: Linha(canvas, cor_primaria)
    }
    ferramenta_atual = ferramentas_disponiveis[modo_atual]

    # LOOP PRINCIPAL
    while janela.esta_aberta():
        glClear(GL_COLOR_BUFFER_BIT) # poe os pixels da janela com a cor de fundo definida

        canvas.desenhar()

        ferramenta_atual.desenhar_previa() # desenha apenas na janela, sem salvar na matriz do canvas

        janela.atualizar_imagem()
        janela.capturar_eventos()
    
    janela.encerrar() # fim do programa

    print("Encerrando programa...")

if __name__ == "__main__":
    main()
