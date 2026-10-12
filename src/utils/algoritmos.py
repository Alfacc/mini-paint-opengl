import numpy as np

# Arquivo para os algoritmos de criar linhas (bresenham), circulos, flood fill...

# usa bresenham para retornar os pontos da linha que sera desenhada
def calcular_linha(x0, y0, x1, y1):
        pontos = []

        x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)

        dist_x = abs(x1 - x0) # distancia/tamanho da linha no eixo x
        dist_y = abs(y1 - y0) # distancia/tamanho da linha no eixo x

        if dist_y == 0: # totalmente horizontal
            for x in range(x0, x1 + 1):
                pontos.append((x, y0))

        elif dist_x == 0: # totalmente vertical
            for y in range(y0, y1 + 1):
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