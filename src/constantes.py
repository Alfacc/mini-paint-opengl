from enum import Enum

class ModoFerramenta(Enum):
    PINCEL = 1
    BORRACHA = 2
    RETA = 3
    CURVA = 4
    RETANGULO_VAZIO = 5
    RETANGULO_CHEIO = 6
    CIRCULO_VAZIO = 7
    CIRCULO_CHEIO = 8
    BALDE = 9

COR_FUNDO_JANELA = (128, 128, 128) # cinza
COR_FUNDO_CANVAS = (255, 255, 255) # branco

class Paleta:
    BRANCO   = (255, 255, 255)
    PRETO    = (0, 0, 0)
    VERMELHO = (255, 0, 0)
    VERDE    = (0, 255, 0)
    AZUL     = (0, 0, 255)
    AMARELO  = (255, 255, 0)
    CIANO    = (0, 255, 255)
    MAGENTA  = (255, 0, 255)

class Espessura:
    FINO = 1    # 1x1 pixel
    MEDIO = 3   # 3x3 pixels (raio = 1 ao redor do centro)
    GROSSO = 5  # 5x5 pixels (raio = 2 ao redor do centro)