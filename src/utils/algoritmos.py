import numpy as np
from collections import deque

# Arquivo para os algoritmos de criar linhas (bresenham), circulos, flood fill...

# usa bresenham para retornar os pontos da linha que sera desenhada
def calcular_linha(x0, y0, x1, y1):
        pontos = []

        x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)

        dist_x = abs(x1 - x0) # distancia/tamanho da linha no eixo x
        dist_y = abs(y1 - y0) # distancia/tamanho da linha no eixo x

        if dist_y == 0: # totalmente horizontal
            if x0 < x1:
                for x in range(x0, x1 + 1): # +1 para incluir o ponto final
                    pontos.append((x, y0))
            else:
                for x in range(x1, x0 + 1): # +1 para incluir o ponto final
                    pontos.append((x, y0))

        elif dist_x == 0: # totalmente vertical
            if y0 < y1:
                for y in range(y0, y1 + 1): # +1 para incluir o ponto final
                    pontos.append((x0, y))
            else:
                for y in range(y1, y0 + 1): # +1 para incluir o ponto final
                    pontos.append((x0, y))

        else: # caso generico
            passo_x = 1 if x0 < x1 else -1 # 1: esq->dir e -1: dir->esq
            passo_y = 1 if y0 < y1 else -1 # 1: cima->baixo e -1: baixo->cima

            err = dist_x - dist_y # err > 0: linha mais horizontal e err < 0: linha mais vertical

            x, y = x0, y0

            while True:
                pontos.append((x, y))

                if x == x1 and y == y1:
                    break

                e2 = 2 * err

                if e2 > -dist_y: 
                    err -= dist_y
                    x += passo_x

                if e2 < dist_x:
                    err += dist_x
                    y += passo_y

        return pontos

# Midpoint
def calcular_circulo(cx, cy, r):

    pontos = []
    x = 0
    y = -r

    # Calcula a distância até o pixel a ser desenhado
    p = -r


    # Calcula uma fatia de 45° graus do círculo
    while x <= -y:
        # Espalhamento para os outros ângulos de 45° graus além dele mesmo
        pontos.append((cx + x, cy + y))
        pontos.append((cx - x, cy + y))
        pontos.append((cx + x, cy - y))
        pontos.append((cx - x, cy - y))
        pontos.append((cx + y, cy + x))
        pontos.append((cx + y, cy - x))
        pontos.append((cx - y, cy + x)) 
        pontos.append((cx - y, cy - x))

        # Pixel fora do meio ponto dentro do círculo
        if p > 0:
            y += 1
            p += 2 * (x + y) + 1

        # Pixel dentro do círculo    
        else:
            p += 2 * x + 1

        x += 1

    return pontos

def calcular_curva(p0, p1, p2, nseg=40):

    pontos = []
    x_anterior, y_anterior = p0

    for i in range(1, nseg+1):
        t = i/nseg

        x = (1-t)**2 * p0[0] + 2 * (1-t) * t * p1[0] + (t**2) * p2[0]
        y = (1-t)**2 * p0[1] + 2 * (1-t) * t * p1[1] + (t**2) * p2[1]

        pontos.extend(calcular_linha(x_anterior, y_anterior, round(x), round(y)))
        x_anterior, y_anterior = round(x), round(y)

    return pontos


def retangulo_cheio(x0, y0, x1, y1):
    pontos = []

    xmin, xmax = min(x0, x1), max(x0, x1)
    ymin, ymax = min(y0, y1), max(y0, y1)

    for y in range(ymin, ymax + 1):
        # Percore a vertical e preenchendo com uma linha a horizontal
        pontos.extend(calcular_linha(xmin, y, xmax, y))

    return pontos

def circulo_cheio(cx, cy, r):
    pontos = []
    
    x = 0
    y = -r
    p = -r

    while x <= -y:
        # Liga a borda esquerda à borda direita em cada uma das 4 alturas simétricas
        pontos.extend(calcular_linha(cx - x, cy + y, cx + x, cy + y))
        pontos.extend(calcular_linha(cx - x, cy - y, cx + x, cy - y))
        pontos.extend(calcular_linha(cx + y, cy + x, cx - y, cy + x))
        pontos.extend(calcular_linha(cx + y, cy - x, cx - y, cy - x))
        if p > 0:
            y += 1
            p += 2 * (x + y) + 1
        else:
            p += 2 * x + 1
        x += 1

    return pontos

def flood_fill(canvas, x0, y0, cor, vizinhanca=4):
    cor_inicial = canvas.get_pixel(x0, y0)

    # Caso clique em algum lugar fora ou cores iguais
    if cor_inicial is None or np.array_equal(cor_inicial, cor):
        return
    cor_alvo = cor_inicial.copy()
    
    # Os dois tipos de vizinhança
    if vizinhanca == 4:
        deslocamentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    else:
        deslocamentos = [(-1, 0), (1, 0), (0, -1), (0, 1),
                         (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
    # deque é igual a uma lista, mas o popleft() é instantâneo (não trava se pintar a tela toda)
    fila = deque([(x0, y0)])
    canvas.put_pixel(x0, y0, cor)

    while len(fila) > 0:
        x, y = fila.popleft()

        # Checagem dos vizinhos
        for dx, dy in deslocamentos:
            novo_x, novo_y = x + dx, y + dy

            cor_vizinha = canvas.get_pixel(novo_x, novo_y)
            
            # Se cor vizinha é 'real' e está na cor alvo, pinta ela
            if cor_vizinha is not None and np.array_equal(cor_vizinha, cor_alvo):
                canvas.put_pixel(novo_x, novo_y, cor)
                fila.append((novo_x, novo_y))

