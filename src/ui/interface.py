import imgui
from constantes import ModoFerramenta, Paleta, Espessura, COR_FUNDO_CANVAS
from core.exportar import Exportar

class InterfaceUI:
    def __init__(self, app_state):
        self.app = app_state
        self.cor_picker = [0.0, 0.0, 0.0]

    def renderizar(self):
        imgui.begin("Painel de Ferramentas", True)

        # ----------------------------------------------------
        # 1. FERRAMENTAS
        # ----------------------------------------------------
        imgui.text("Ferramentas")
        
        m_atual = self.app['modo_atual']

        if imgui.radio_button("Pincel (1)", m_atual == ModoFerramenta.PINCEL):
            self.definir_ferramenta(ModoFerramenta.PINCEL)
        imgui.same_line()
        if imgui.radio_button("Borracha (2)", m_atual == ModoFerramenta.BORRACHA):
            self.definir_ferramenta(ModoFerramenta.BORRACHA)

        if imgui.radio_button("Reta (3)", m_atual == ModoFerramenta.RETA):
            self.definir_ferramenta(ModoFerramenta.RETA)
        imgui.same_line()
        if imgui.radio_button("Curva (4)", m_atual == ModoFerramenta.CURVA):
            self.definir_ferramenta(ModoFerramenta.CURVA)

        if imgui.radio_button("Ret. Vazio (5)", m_atual == ModoFerramenta.RETANGULO_VAZIO):
            self.definir_ferramenta(ModoFerramenta.RETANGULO_VAZIO)
        imgui.same_line()
        if imgui.radio_button("Ret. Cheio (6)", m_atual == ModoFerramenta.RETANGULO_CHEIO):
            self.definir_ferramenta(ModoFerramenta.RETANGULO_CHEIO)

        if imgui.radio_button("Circ. Vazio (7)", m_atual == ModoFerramenta.CIRCULO_VAZIO):
            self.definir_ferramenta(ModoFerramenta.CIRCULO_VAZIO)
        imgui.same_line()
        if imgui.radio_button("Circ. Cheio (8)", m_atual == ModoFerramenta.CIRCULO_CHEIO):
            self.definir_ferramenta(ModoFerramenta.CIRCULO_CHEIO)

        if imgui.radio_button("Balde (9)", m_atual == ModoFerramenta.BALDE):
            self.definir_ferramenta(ModoFerramenta.BALDE)

        imgui.separator()

        # ----------------------------------------------------
        # 2. ESPESSURA
        # ----------------------------------------------------
        imgui.text("Espessura")
        esp_atual = self.app['canvas'].espessura

        if imgui.radio_button("Fino (1px - P)", esp_atual == Espessura.FINO):
            self.app['canvas'].espessura = Espessura.FINO
        imgui.same_line()
        if imgui.radio_button("Médio (3px - M)", esp_atual == Espessura.MEDIO):
            self.app['canvas'].espessura = Espessura.MEDIO
        imgui.same_line()
        if imgui.radio_button("Grosso (5px - G)", esp_atual == Espessura.GROSSO):
            self.app['canvas'].espessura = Espessura.GROSSO

        imgui.separator()

        # ----------------------------------------------------
        # 3. PALETA DE CORES
        # ----------------------------------------------------
        imgui.text("Paleta de Cores")

        cores = [
            ("Preto", Paleta.PRETO),
            ("Branco", Paleta.BRANCO),
            ("Vermelho", Paleta.VERMELHO),
            ("Verde", Paleta.VERDE),
            ("Azul", Paleta.AZUL),
            ("Amarelo", Paleta.AMARELO),
            ("Ciano", Paleta.CIANO),
            ("Magenta", Paleta.MAGENTA),
        ]

        for i, (nome, cor_rgb) in enumerate(cores):
            if imgui.button(nome):
                self.atualizar_cor(cor_rgb)
            if (i + 1) % 4 != 0:
                imgui.same_line()

        # Seletor livre RGB
        changed, nova_cor = imgui.color_edit3("Cor Personalizada", *self.cor_picker)
        if changed:
            self.cor_picker = list(nova_cor)
            cor_int = (int(nova_cor[0]*255), int(nova_cor[1]*255), int(nova_cor[2]*255))
            self.atualizar_cor(cor_int)

        imgui.separator()

        # ----------------------------------------------------
        # 4. AÇÕES DA TELA
        # ----------------------------------------------------
        if imgui.button("Novo Canvas (R)"):
            self.app['canvas'].limpar()

        imgui.same_line()
        if imgui.button("Salvar (S)"):
            Exportar(self.app['canvas'], "desenho.png")

        imgui.end()

    def definir_ferramenta(self, modo):
        self.app['modo_atual'] = modo
        self.app['ferramenta_atual'] = self.app['ferramentas'][modo]

    def atualizar_cor(self, cor_rgb):
        self.app['cor_primaria'] = cor_rgb
        self.cor_picker = [cor_rgb[0]/255.0, cor_rgb[1]/255.0, cor_rgb[2]/255.0]

        # Atualiza a cor de todas as ferramentas ativas exceto a borracha
        for modo, ferra in self.app['ferramentas'].items():
            if modo != ModoFerramenta.BORRACHA:
                ferra.cor = cor_rgb