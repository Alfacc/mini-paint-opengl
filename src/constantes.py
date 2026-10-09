from enum import Enum

class ModoFerramenta(Enum):
    PINCEL = 1 # pincel/lapis
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

