import glfw
from OpenGL.GL import *
import imgui
from imgui.integrations.glfw import GlfwRenderer

from core.janela import Janela
from core.canvas import Canvas
from core.exportar import Exportar
from constantes import *
from ferramentas import Pincel, Borracha, Curva, Reta, RetanguloVazio, RetanguloCheio, CirculoVazio, CirculoCheio, Balde
from ui.interface import InterfaceUI

def main():
    print("Iniciando programa...")

    janela = Janela(1200, 900, "Mini Paint", COR_FUNDO_JANELA)

    estado = janela.inicializar()
    if estado == 1:
        print("Não foi possível inicializar o GLFW.")
        return
    elif estado == 2:
        print("Erro ao criar janela.")
        return
    else:
        print("Janela criada com sucesso.")

    # Inicializa o Dear ImGui
    imgui.create_context()
    impl = GlfwRenderer(janela.referencia)

    # Projeção 2D do OpenGL
    glMatrixMode(GL_PROJECTION)
    glOrtho(0, janela.largura, janela.altura, 0, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    canvas = Canvas(800, 600, COR_FUNDO_CANVAS, (janela.largura, janela.altura))

    cor_primaria = Paleta.PRETO

    ferramentas_disponiveis = {
        ModoFerramenta.PINCEL: Pincel(canvas, cor_primaria),
        ModoFerramenta.BORRACHA: Borracha(canvas, COR_FUNDO_CANVAS),
        ModoFerramenta.CURVA: Curva(canvas, cor_primaria),
        ModoFerramenta.RETA: Reta(canvas, cor_primaria),
        ModoFerramenta.RETANGULO_VAZIO: RetanguloVazio(canvas, cor_primaria),
        ModoFerramenta.RETANGULO_CHEIO: RetanguloCheio(canvas, cor_primaria),
        ModoFerramenta.CIRCULO_VAZIO: CirculoVazio(canvas, cor_primaria),
        ModoFerramenta.CIRCULO_CHEIO: CirculoCheio(canvas, cor_primaria),
        ModoFerramenta.BALDE: Balde(canvas, cor_primaria)
    }

    # Estado compartilhado com a Interface UI
    app_state = {
        'canvas': canvas,
        'modo_atual': ModoFerramenta.PINCEL,
        'ferramentas': ferramentas_disponiveis,
        'ferramenta_atual': ferramentas_disponiveis[ModoFerramenta.PINCEL],
        'cor_primaria': cor_primaria
    }

    interface_ui = InterfaceUI(app_state)

    # CALLBACKS
    def callback_botao_mouse(win, botao, acao, mods):
        impl.mouse_callback(win, botao, acao, mods)
        
        # Não desenha se o clique for dentro do painel do ImGui
        io = imgui.get_io()
        if io.want_capture_mouse:
            return

        x, y = glfw.get_cursor_pos(win)
        x, y = int(x), int(y)

        ferramenta_atual = app_state['ferramenta_atual']

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

    def callback_movimento_mouse(win, pos_x, pos_y):
        io = imgui.get_io()
        if io.want_capture_mouse:
            return

        x, y = int(pos_x), int(pos_y)

        ferramenta_atual = app_state['ferramenta_atual']

        estado_esquerdo = glfw.get_mouse_button(win, glfw.MOUSE_BUTTON_LEFT)
        if estado_esquerdo == glfw.PRESS:
            ferramenta_atual.arrastar_esquerdo(x, y)
            
        estado_direito = glfw.get_mouse_button(win, glfw.MOUSE_BUTTON_RIGHT)
        if estado_direito == glfw.PRESS:
            ferramenta_atual.arrastar_direito(x, y)

    def callback_teclado(win, tecla, scancode, acao, mods):
        impl.keyboard_callback(win, tecla, scancode, acao, mods)
        io = imgui.get_io()
        if io.want_capture_keyboard:
            return

        if acao == glfw.PRESS:
            if tecla == glfw.KEY_R:
                app_state['canvas'].limpar()
            elif tecla == glfw.KEY_S:
                Exportar(app_state['canvas'], "desenho.png")
            elif tecla == glfw.KEY_1:
                interface_ui.definir_ferramenta(ModoFerramenta.PINCEL)
            elif tecla == glfw.KEY_2:
                interface_ui.definir_ferramenta(ModoFerramenta.BORRACHA)
            elif tecla == glfw.KEY_3:
                interface_ui.definir_ferramenta(ModoFerramenta.RETA)
            elif tecla == glfw.KEY_4:
                interface_ui.definir_ferramenta(ModoFerramenta.CURVA)
            elif tecla == glfw.KEY_5:
                interface_ui.definir_ferramenta(ModoFerramenta.RETANGULO_VAZIO)
            elif tecla == glfw.KEY_6:
                interface_ui.definir_ferramenta(ModoFerramenta.RETANGULO_CHEIO)
            elif tecla == glfw.KEY_7:
                interface_ui.definir_ferramenta(ModoFerramenta.CIRCULO_VAZIO)
            elif tecla == glfw.KEY_8:
                interface_ui.definir_ferramenta(ModoFerramenta.CIRCULO_CHEIO)
            elif tecla == glfw.KEY_9:
                interface_ui.definir_ferramenta(ModoFerramenta.BALDE)
            elif tecla == glfw.KEY_P:
                app_state['canvas'].espessura = Espessura.FINO
            elif tecla == glfw.KEY_M:
                app_state['canvas'].espessura = Espessura.MEDIO
            elif tecla == glfw.KEY_G:
                app_state['canvas'].espessura = Espessura.GROSSO

    # Registra callbacks no GLFW
    glfw.set_mouse_button_callback(janela.referencia, callback_botao_mouse)
    glfw.set_cursor_pos_callback(janela.referencia, callback_movimento_mouse)
    glfw.set_key_callback(janela.referencia, callback_teclado)

    # LOOP PRINCIPAL
    while janela.esta_aberta():
        glfw.poll_events()
        impl.process_inputs()

        glClear(GL_COLOR_BUFFER_BIT)

        # Desenha o Canvas e as prévias no OpenGL
        canvas.desenhar()
        app_state['ferramenta_atual'].desenhar_previa()

        # Renderização do ImGui
        imgui.new_frame()
        interface_ui.renderizar()
        imgui.render()
        impl.render(imgui.get_draw_data())

        janela.atualizar_imagem()

    impl.shutdown()
    janela.encerrar()
    print("Encerrando programa...")

if __name__ == "__main__":
    main()