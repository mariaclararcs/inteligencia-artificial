import numpy as np
import random as rd

def Gera_Problema_Grid_Fixo(arquivo):
    f = open(arquivo,"r")
    
    mapa = []
    for str1 in f:
        str1 = str1.strip("\n")
        str1 = str1.split(",")
        int_str1 = []
        for s in str1:
            int_str1.append(int(s))
        mapa.append(int_str1)
    
    return mapa


def Gera_Problema_Grid(n,m,qt_ob):
    mapa = np.zeros((n,m),int)
    
    if qt_ob>n*m:
        return "ERRO"
    o = 0
    while o<qt_ob:
        i = rd.randrange(0,n)
        j = rd.randrange(0,m)
        if mapa[i][j]==0:
            mapa[i][j]=9
            o +=1
    return mapa
        
"""    
    f = open(arquivo,"r")
    
    mapa = []
    for str1 in f:
        str1 = str1.strip("\n")
        str1 = str1.split(",")
        for i in range(len(str1)):
            str1[i] = int(str1[i])
        mapa.append(str1)
    return mapa
"""    

def sucessor_grid(x,y,dx,dy,mapa):
    f = []

    # acima
    if y+1<dy:
        if mapa[x][y+1]!=9:
            linha = []
            linha.append(x)
            linha.append(y+1)
            f.append(linha)
    
    # esquerda
    if x-1>=0:
        if mapa[x-1][y]!=9:
            linha = []
            linha.append(x-1)
            linha.append(y)
            f.append(linha)

    # direita
    if x+1<dx:
        if mapa[x+1][y]!=9:
            linha = []
            linha.append(x+1)
            linha.append(y)
            f.append(linha)

    # abaixo
    if y-1>=0:
        if mapa[x][y-1]!=9:
            linha = []
            linha.append(x)
            linha.append(y-1)
            f.append(linha)
    
    if x+1<dx and y-1>=0:
        if mapa[x+1][y-1]!=9:
            linha = []
            linha.append(x+1)
            linha.append(y-1)
            f.append(linha)
    
    if x+1<dx and y+1<dy:
        if mapa[x+1][y+1]!=9:
            linha = []
            linha.append(x+1)
            linha.append(y+1)
            f.append(linha)
    
    if x-1>=0 and y-1>=0:
        if mapa[x-1][y-1]!=9:
            linha = []
            linha.append(x-1)
            linha.append(y-1)
            f.append(linha)
    
    if x-1>=0 and y+1<dy:
        if mapa[x-1][y+1]!=9:
            linha = []
            linha.append(x-1)
            linha.append(y+1)
            f.append(linha)
    
    return f
