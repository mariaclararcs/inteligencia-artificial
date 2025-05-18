from busca_sem_pesos import buscaGridNP  
import numpy as np
from random import randrange

def Gera_Problema(nx,ny,qtd):
    mapa = np.zeros((nx,ny),int)
    
    k = 0
    while k<qtd:
        i = randrange(0,nx)
        j = randrange(0,ny)
        if mapa[i][j]==0:
            mapa[i][j] = 9
            k+=1
    return mapa


# PROGRAMA PRINCIPAL
nx  = 10
ny  = 10
qtd = 10
mapa = Gera_Problema(nx,ny,qtd)


print("======== Mapa ========\n",mapa)
print()

sol = buscaGridNP()
caminho = []


while True:
    print("Coordenada da origem: ")
    x  = int(input("X = "))
    y = int(input("Y =  "))
    if mapa[x][y]==0:
        break
    print("Coordenada inválida")

origem = [x,y]

while True:
    print("Coordenada do destino: ")
    x  = int(input("X = "))
    y = int(input("Y =  "))
    if mapa[x][y]==0:
        break
    print("Coordenada inválida")

destino = [x,y]

caminho = sol.amplitude(origem,destino,nx,ny,mapa)
if caminho!=None:
    print("\n*****AMPLITUDE*****")
    print("Caminho: ",caminho)
    print("Custo..: ",len(caminho)-1)
else:
    print("CAMINHO NÃO ENCONTRADO")
      
caminho = sol.profundidade(origem,destino,nx,ny,mapa)
if caminho!=None:
    print("\n*****PROFUNDIDADE*****")
    print("Caminho: ",caminho)
    print("Custo..: ",len(caminho)-1)
else:
    print("CAMINHO NÃO ENCONTRADO")
      
limite = 10
caminho = sol.prof_limitada(origem,destino,nx,ny,mapa,limite)
if caminho!=None:
    print("\n*****PROFUNDIDADE LIMITADA*****")
    print("Caminho: ",caminho)
    print("Custo..: ",len(caminho)-1)
else:
    print("CAMINHO NÃO ENCONTRADO")

   
limite_maximo = nx*ny
caminho = sol.aprof_iterativo(origem,destino,nx,ny,mapa,limite_maximo)
if caminho!=None:
    print("\n*****APROFUNDAMENTO ITERATIVO*****")
    print("Caminho: ",caminho)
    print("Custo..: ",len(caminho)-1)
else:
    print("CAMINHO NÃO ENCONTRADO")


caminho = sol.bidirecional(origem,destino,nx,ny,mapa)
if caminho!=None:
    print("\n*****BIDIRECIONAL*****")
    print("Caminho: ",caminho)
    print("Custo..: ",len(caminho)-1)
else:
    print("CAMINHO NÃO ENCONTRADO")
