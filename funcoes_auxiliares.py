from math import sqrt

def sucessores(atual, mapa, dim_x, dim_y):
    f = []
    x = atual[0]
    y = atual[1]
    
    # Movimento para baixo (y+1) - Custo 1
    if y+1 < dim_y:
        if mapa[y+1][x] == 0:  # Verifica se é caminho livre (0)
            f.append([x, y+1, 1])
            
    # Movimento para direita (x+1) - Custo 3
    if x+1 < dim_x:
        if mapa[y][x+1] == 0:  # Verifica se é caminho livre (0)
            f.append([x+1, y, 3])
            
    # Movimento para esquerda (x-1) - Custo 2
    if x-1 >= 0:
        if mapa[y][x-1] == 0:  # Verifica se é caminho livre (0)
            f.append([x-1, y, 2])
            
    # Movimento para cima (y-1) - Custo 4
    if y-1 >= 0:
        if mapa[y-1][x] == 0:  # Verifica se é caminho livre (0)
            f.append([x, y-1, 4])
            
    return f

def Gera_Ambiente(arquivo):
    with open(arquivo, "r") as f:
        mapa = []
        for linha in f:
            linha = linha.strip().split(",")
            mapa.append([int(num) for num in linha])
    return mapa, len(mapa[0]), len(mapa)  # Retorna (mapa, dim_x, dim_y)

def h(p1, p2):
    # Função heurística que considera os custos diferentes para cada direção
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    
    # Custo mínimo estimado considerando movimentos otimizados
    h = min(dx * 2 + dy * 1,  # Priorizando horizontais
            dx * 3 + dy * 4,   # Priorizando verticais
            dx * 2 + dy * 4,    # Combinações
            dx * 3 + dy * 1)
    
    return h