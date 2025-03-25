import tkinter as tk
from tkinter import ttk
from principalBuscaSemPesosGrid import Gera_Problema
from buscaGridNP import buscaGridNP  # Importa a classe de busca

# Criar uma instância da classe busca
buscador = buscaGridNP()

# Carregar a grid do arquivo
mapa = Gera_Problema_Grid_Fixo("exemplo_grid.txt")
GRID_HEIGHT = len(mapa)
GRID_WIDTH = len(mapa[0])
CELL_SIZE = 30

# Criar a janela principal
janela = tk.Tk()
janela.title("Busca em Grafos")
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

# Dicionário para mapear os métodos às funções
metodos_busca = {
    "Amplitude": buscador.amplitude,
    "Profundidade": buscador.profundidade,
    "Profundidade Limitada": buscador.prof_limitada,
    "Aprofundamento Iterativo": buscador.aprof_iterativo,
    "Bidirecional": buscador.bidirecional
}

# ---- Área direita (Grid e Texto) ----
frame_grid = tk.Frame(frame_direita, bg="white")
frame_grid.pack(expand=True, fill="both", padx=20, pady=20)

# Criando um Canvas para desenhar a grid
canvas = tk.Canvas(frame_grid, bg="white", width=GRID_WIDTH * CELL_SIZE, height=GRID_HEIGHT * CELL_SIZE)
canvas.pack()

label_resultado = tk.Label(frame_direita, text="", font=("Arial", 12, "bold"), fg="blue")
label_resultado.pack(pady=10)

# Função para desenhar a grid
def desenhar_grid(caminho=[], inicio=None, fim=None):
    canvas.delete("all")
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            cor = "white" if mapa[y][x] == 0 else "black"
            if (x, y) in caminho:
                cor = "green"  # Caminho encontrado
            if (x, y) == inicio or (x, y) == fim:
                cor = "yellow"  # Ponto inicial e final
            canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, (x+1) * CELL_SIZE, (y+1) * CELL_SIZE, fill=cor, outline="gray")

desenhar_grid()

# Centralizando o canvas dentro do frame_grid
canvas.place(relx=0.5, rely=0.5, anchor="center")

# Função para chamar o método de busca correspondente
def executar_busca():
    metodo = metodo_selecionado.get()
    
    if metodo not in metodos_busca:
        label_resultado.config(text="Selecione um método válido.")
        return

    try:
        inicio = (int(entry_InicioX.get()), int(entry_InicioY.get()))
        fim = (int(entry_ObjetivoX.get()), int(entry_ObjetivoY.get()))
        dx, dy = GRID_WIDTH, GRID_HEIGHT

        if metodo == "Profundidade Limitada":
            limite = 10  # Defina o limite adequado
            caminho = metodos_busca[metodo](inicio, fim, mapa, dx, dy, limite)
        elif metodo == "Aprofundamento Iterativo":
            lim_max = 20  # Defina o limite máximo adequado
            caminho = metodos_busca[metodo](inicio, fim, mapa, dx, dy, lim_max)
        else:
            caminho = metodos_busca[metodo](inicio, fim, mapa, dx, dy)

        if caminho:
            desenhar_grid(caminho, inicio, fim)
            label_resultado.config(text=f"Caminho encontrado: {caminho}")
        else:
            label_resultado.config(text="Nenhum caminho encontrado.")
            desenhar_grid([], inicio, fim)
    
    except ValueError:
        label_resultado.config(text="Erro: Certifique-se de que os valores de entrada são números válidos.")

# Botão para executar a busca
btn_executar = tk.Button(frame_inputs, text="Executar Busca", command=executar_busca)
btn_executar.grid(row=8, column=0, columnspan=2, pady=20)

janela.mainloop()
