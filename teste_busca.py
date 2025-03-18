from busca_sem_pesos_grid import busca
from funcoes_auxiliares import Gera_Problema_Grid_Fixo

# Criar uma instância da classe busca
buscador = busca()

# Carregar a grid de exemplo
mapa = Gera_Problema_Grid_Fixo("exemplo_grid.txt")

# Definir os pontos de início e fim
inicio = (0, 0)  # Exemplo de ponto inicial
fim = (4, 4)  # Exemplo de ponto objetivo

dx = len(mapa[0])  # Largura da grid
dy = len(mapa)  # Altura da grid

# Testar busca em largura (Amplitude)
print("Teste - Busca em Amplitude")
caminho_amplitude = buscador.amplitude(inicio, fim, mapa, dx, dy)
print("Caminho encontrado:", caminho_amplitude)

# Testar busca em profundidade
print("\nTeste - Busca em Profundidade")
caminho_profundidade = buscador.profundidade(inicio, fim, mapa, dx, dy)
print("Caminho encontrado:", caminho_profundidade)

# Testar busca em profundidade limitada
limite = 10
print("\nTeste - Busca em Profundidade Limitada (limite=10)")
caminho_profundidade_limitada = buscador.prof_limitada(inicio, fim, mapa, dx, dy, limite)
print("Caminho encontrado:", caminho_profundidade_limitada)

# Testar busca em aprofundamento iterativo
lim_max = 20
print("\nTeste - Busca em Aprofundamento Iterativo (limite máximo=20)")
caminho_aprof_iterativo = buscador.aprof_iterativo(inicio, fim, mapa, dx, dy, lim_max)
print("Caminho encontrado:", caminho_aprof_iterativo)

# Testar busca bidirecional
print("\nTeste - Busca Bidirecional")
caminho_bidirecional = buscador.bidirecional(inicio, fim, mapa, dx, dy)
print("Caminho encontrado:", caminho_bidirecional)