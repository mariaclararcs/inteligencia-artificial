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

# ---- Área direita (Grid e Texto) ----
frame_grid = tk.Frame(frame_direita, bg="white")
frame_grid.pack(expand=True, fill="both", padx=20, pady=20)

# Canvas para desenhar a grid
CELL_SIZE = 30  # Tamanho das células

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
                                
    # Centralizando o canvas dentro do frame_grid
    canvas.place(relx=0.5, rely=0.5, anchor="center")

busca = buscaGridNP()

# ---- Função para executar a busca ----
def executar_busca():
    metodos_disponiveis = {
    "Amplitude": busca.amplitude,
    "Profundidade": busca.profundidade,
    "Profundidade Limitada": busca.prof_limitada,
    "Aprofundamento Iterativo": busca.aprof_iterativo,
    "Bidirecional": busca.bidirecional  # Caso tenha implementado
    }

    try:
        inicio_x = int(entry_InicioX.get())
        inicio_y = int(entry_InicioY.get())
        objetivo_x = int(entry_ObjetivoX.get())
        objetivo_y = int(entry_ObjetivoY.get())
        
        matriz = carregar_matriz()
        
        if not matriz:
            return
        
        metodo = metodo_selecionado.get()
        
        if metodo not in metodos_disponiveis:
            label_resultado.config(text="Selecione um método válido", fg="red")
            return
        
        nx, ny = len(matriz), len(matriz[0])  # Dimensões da matriz
        inicio = [inicio_x, inicio_y]
        objetivo = [objetivo_x, objetivo_y]

        # Chama a busca correspondente
        if metodo == "Profundidade Limitada":
            caminho = metodos_disponiveis[metodo](inicio, objetivo, nx, ny, matriz, 10)  # Limiar arbitrário 10
        elif metodo == "Aprofundamento Iterativo":
            caminho = metodos_disponiveis[metodo](inicio, objetivo, nx, ny, matriz, 20)  # Profundidade máxima 20
        else:
            caminho = metodos_disponiveis[metodo](inicio, objetivo, nx, ny, matriz)

        if caminho:
            caminho = [(estado[0], estado[1]) for estado in caminho]  # Converte para tuplas
            desenhar_grid(matriz, caminho, inicio=tuple(inicio), fim=tuple(objetivo))
            label_resultado.config(text="Caminho encontrado!", fg="green")
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

janela.mainloop()