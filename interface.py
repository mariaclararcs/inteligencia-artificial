import tkinter as tk
from tkinter import ttk
from buscaGridNP import buscaGridNP

# Criar a janela principal
janela = tk.Tk()
janela.title("Busca em Grid")
janela.state('zoomed')

# Criando os frames principais
frame_esquerda = tk.Frame(janela, width=400)
frame_esquerda.pack(side="left", fill="y")
frame_esquerda.pack_propagate(False)

frame_direita = tk.Frame(janela)
frame_direita.pack(side="right", expand=True, fill="both")

# ---- Área esquerda (Inputs e Botão) ----
frame_inputs = tk.Frame(frame_esquerda)
frame_inputs.pack(pady=20, padx=20)

# Campos de entrada
tk.Label(frame_inputs, text="Início", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(frame_inputs, text="X:").grid(row=1, column=0, sticky="e", pady=5)
entry_InicioX = tk.Entry(frame_inputs)
entry_InicioX.grid(row=1, column=1, pady=5)

tk.Label(frame_inputs, text="Y:").grid(row=2, column=0, sticky="e", pady=5)
entry_InicioY = tk.Entry(frame_inputs)
entry_InicioY.grid(row=2, column=1, pady=5)

tk.Label(frame_inputs, text="Objetivo", font=("Arial", 12, "bold")).grid(row=3, column=0, columnspan=2, pady=10)

tk.Label(frame_inputs, text="X:").grid(row=4, column=0, sticky="e", pady=5)
entry_ObjetivoX = tk.Entry(frame_inputs)
entry_ObjetivoX.grid(row=4, column=1, pady=5)

tk.Label(frame_inputs, text="Y:").grid(row=5, column=0, sticky="e", pady=5)
entry_ObjetivoY = tk.Entry(frame_inputs)
entry_ObjetivoY.grid(row=5, column=1, pady=5)

# Dropdown para escolher o método de busca
tk.Label(frame_inputs, text="Métodos:", font=("Arial", 12, "bold")).grid(row=6, column=0, columnspan=2, pady=10)
metodos = ["Amplitude", "Profundidade", "Profundidade Limitada", "Aprofundamento Iterativo", "Bidirecional"]
metodo_selecionado = tk.StringVar()
dropdown_metodo = ttk.Combobox(frame_inputs, textvariable=metodo_selecionado, values=metodos)
dropdown_metodo.grid(row=7, column=0, columnspan=2, pady=5)

# ---- Área direita (Grid e Resultado) ----
frame_grid = tk.Frame(frame_direita, bg="white")
frame_grid.pack(expand=True, fill="both", padx=20, pady=20)

# Canvas para desenhar a grid
CELL_SIZE = 30  # Tamanho das células

inicio_coord = None
objetivo_coord = None
selecionando_inicio = True  # Para alternar entre início e objetivo

canvas = tk.Canvas(frame_grid, bg="white")
canvas.pack(expand=True, fill="both")

label_resultado = tk.Label(frame_direita, text="", font=("Arial", 12, "bold"), fg="blue")
label_resultado.pack(pady=10)

# ---- Função para ler a matriz do arquivo ----
def carregar_matriz():
    try:
        with open("exemplo_grid.txt", "r") as file:
            matriz = []
            for linha in file:
                numeros = linha.split(",")
                matriz.append([int(num) for num in numeros])  # Converte para inteiros
            return matriz
    except FileNotFoundError:
        print("Erro: Arquivo 'exemplo_grid.txt' não encontrado.")
        return []
    except ValueError as e:
        print(f"Erro ao processar o arquivo: {e}")
        return []

# ---- Função para desenhar a grid ----
def desenhar_grid(matriz, caminho=[], inicio=None, fim=None):
    canvas.delete("all")
    
    linhas = len(matriz)
    colunas = len(matriz[0]) if matriz else 0

    canvas.config(width=colunas * CELL_SIZE, height=linhas * CELL_SIZE)

    for y in range(linhas):
        for x in range(colunas):
            cor = "white"  # Caminho livre por padrão

            if matriz[y][x] == 9:
                cor = "black"  # Obstáculo
            if (x, y) in caminho:
                cor = "green"  # Caminho encontrado
            if (x, y) == inicio:
                cor = "yellow"  # Ponto inicial
            if (x, y) == fim:
                cor = "red"  # Ponto final

            canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, 
                                    (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, 
                                    fill=cor, outline="gray")
                                 
    canvas.place(relx=0.5, rely=0.5, anchor="center")

def selecionar_ponto(event):
    global inicio_coord, objetivo_coord, selecionando_inicio

    # Obter coordenadas clicadas no grid
    x = event.x // CELL_SIZE
    y = event.y // CELL_SIZE

    matriz = carregar_matriz()
    if not matriz:
        return

    # Evita selecionar um obstáculo como início ou objetivo
    if matriz[y][x] == 9:
        return

    if selecionando_inicio:
        inicio_coord = (x, y)
        entry_InicioX.delete(0, tk.END)
        entry_InicioX.insert(0, str(x))
        entry_InicioY.delete(0, tk.END)
        entry_InicioY.insert(0, str(y))
    else:
        objetivo_coord = (x, y)
        entry_ObjetivoX.delete(0, tk.END)
        entry_ObjetivoX.insert(0, str(x))
        entry_ObjetivoY.delete(0, tk.END)
        entry_ObjetivoY.insert(0, str(y))

    # Alternar para selecionar o outro ponto na próxima vez
    selecionando_inicio = not selecionando_inicio

    # Redesenhar grid com os pontos atualizados
    desenhar_grid(matriz, inicio=inicio_coord, fim=objetivo_coord)

busca = buscaGridNP()

# ---- Função para verificar se existe um caminho alcançável ----
def verificar_conexao(inicio, objetivo, nx, ny, matriz):
    visitados = set()
    fila = [inicio]
    
    while fila:
        x, y = fila.pop(0)
        
        # Se o objetivo for encontrado
        if (x, y) == objetivo:
            return True
        
        if (x, y) in visitados:
            continue
        
        visitados.add((x, y))
        
        # Verificar vizinhos (4 direções)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            # Verificar se o vizinho está dentro dos limites da matriz e não é um obstáculo
            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]) and matriz[ny][nx] != 9:
                fila.append((nx, ny))
    
    return False

# ---- Função para executar a busca ----
def executar_busca():
    metodos_disponiveis = {
    "Amplitude": busca.amplitude,
    "Profundidade": busca.profundidade,
    "Profundidade Limitada": busca.prof_limitada,
    "Aprofundamento Iterativo": busca.aprof_iterativo,
    "Bidirecional": busca.bidirecional
    }

    try:
        inicio_x = int(entry_InicioX.get())
        inicio_y = int(entry_InicioY.get())
        objetivo_x = int(entry_ObjetivoX.get())
        objetivo_y = int(entry_ObjetivoY.get())
        
        matriz = carregar_matriz()
        
        if not matriz:
            return

        nx, ny = len(matriz), len(matriz[0])  # Dimensões da matriz

        # Verifica se as coordenadas estão dentro dos limites da matriz
        if not (0 <= inicio_x < ny and 0 <= inicio_y < nx):
            label_resultado.config(text="Erro: Coordenada de início fora do grid!", fg="red")
            return
        
        if not (0 <= objetivo_x < ny and 0 <= objetivo_y < nx):
            label_resultado.config(text="Erro: Coordenada de objetivo fora do grid!", fg="red")
            return

        # Verifica se o início ou o objetivo são obstáculos
        if matriz[inicio_y][inicio_x] == 9:
            label_resultado.config(text="Erro: O ponto de início é um obstáculo!", fg="red")
            return

        if matriz[objetivo_y][objetivo_x] == 9:
            label_resultado.config(text="Erro: O ponto de objetivo é um obstáculo!", fg="red")
            return
        
        # Verificar se o caminho entre o início e o objetivo está bloqueado
        if not verificar_conexao((inicio_x, inicio_y), (objetivo_x, objetivo_y), nx, ny, matriz):
            label_resultado.config(text="Erro: O caminho entre o início e o objetivo está bloqueado por obstáculos!", fg="red")
            return

        metodo = metodo_selecionado.get()

        if metodo not in metodos_disponiveis:
            label_resultado.config(text="Selecione um método válido", fg="red")
            return
        
        inicio = [inicio_x, inicio_y]
        objetivo = [objetivo_x, objetivo_y]

        # Chama a busca correspondente
        if metodo == "Profundidade Limitada":
            caminho = metodos_disponiveis[metodo](inicio, objetivo, nx, ny, matriz, 10)  # Limite 10
        elif metodo == "Aprofundamento Iterativo":
            caminho = metodos_disponiveis[metodo](inicio, objetivo, nx, ny, matriz, 20)  # Profundidade 20
        else:
            caminho = metodos_disponiveis[metodo](inicio, objetivo, nx, ny, matriz)

        if caminho:
            caminho = [(estado[0], estado[1]) for estado in caminho]
            desenhar_grid(matriz, caminho, inicio=tuple(inicio), fim=tuple(objetivo))

            caminho_str = " > ".join([f"({x}, {y})" for x, y in caminho])
            label_resultado.config(text=f"Caminho encontrado:\n{caminho_str}", fg="green")
        else:
            label_resultado.config(text="Nenhum caminho encontrado!", fg="red")

    except ValueError:
        print("Erro: Certifique-se de que todas as coordenadas são números inteiros.")

# Botão para executar a busca
btn_executar = tk.Button(frame_inputs, text="Executar Busca", command=executar_busca)
btn_executar.grid(row=8, column=0, columnspan=2, pady=20)

# Carregar e desenhar a matriz ao iniciar
matriz_inicial = carregar_matriz()
desenhar_grid(matriz_inicial)

canvas.bind("<Button-1>", selecionar_ponto)
janela.mainloop()