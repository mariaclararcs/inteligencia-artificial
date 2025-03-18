import tkinter as tk
from tkinter import ttk
from funcoes_auxiliares import Gera_Problema_Grid_Fixo

# Carregar a grid do arquivo
mapa = Gera_Problema_Grid_Fixo("exemplo_grid.txt")
GRID_HEIGHT = len(mapa)  # Define a altura como o número de linhas
GRID_WIDTH = len(mapa[0])  # Define a largura como o número de colunas
CELL_SIZE = 30  # Tamanho de cada célula em pixels

janela = tk.Tk()
janela.title("A-estrela")
janela.state('zoomed')

# Criando os frames principais com ajuste de largura
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

# Dropdown
tk.Label(frame_inputs, text="Métodos:", font=("Arial", 12, "bold")).grid(row=6, column=0, columnspan=2, pady=10)
opcoes = ["", "Amplitude", "Profundidade", "Profundidade Limitada", "Aprofundamento Iterativo", "Bidirecional"]
dropdown = ttk.Combobox(frame_inputs, value=opcoes)
dropdown.grid(row=7, column=0, columnspan=2, pady=5)
dropdown.current(0)

# Função para capturar os valores inseridos pelo usuário
def salvar_valores():
    """Captura os valores dos inputs e salva em variáveis."""
    inicio_x = entry_InicioX.get()
    inicio_y = entry_InicioY.get()
    objetivo_x = entry_ObjetivoX.get()
    objetivo_y = entry_ObjetivoY.get()
    metodo_escolhido = dropdown.get()

    print(f"Início: ({inicio_x}, {inicio_y})")
    print(f"Objetivo: ({objetivo_x}, {objetivo_y})")
    print(f"Método escolhido: {metodo_escolhido}")

# Botão
btn_Executar = tk.Button(frame_esquerda, text="Executar", command=salvar_valores)
btn_Executar.pack(pady=20)

# ---- Área direita (Grid e Texto) ----
frame_grid = tk.Frame(frame_direita, bg="white")
frame_grid.pack(expand=True, fill="both", padx=20, pady=20)

# Criando um Canvas para desenhar a grid
canvas = tk.Canvas(frame_grid, bg="white", width=GRID_WIDTH * CELL_SIZE, height=GRID_HEIGHT * CELL_SIZE)
canvas.pack()

def desenhar_grid():
    """Função para desenhar a grade no Canvas de acordo com o arquivo"""
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            x1, y1 = j * CELL_SIZE, i * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
            cor = "black" if mapa[i][j] == 9 else "white"
            canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=cor)

desenhar_grid()

# Centralizando o canvas dentro do frame_grid
canvas.place(relx=0.5, rely=0.5, anchor="center")

# Campo de resultado
label_resultado = tk.Label(frame_direita, text="Resultado aparecerá aqui", fg="blue", font=("Arial", 12, "bold"))
label_resultado.pack(pady=10)

janela.mainloop()