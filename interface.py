import tkinter as tk
from tkinter import ttk

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
opcoes = ["", "Amplitude", "Profundidade Limitada", "Aprofundamento Iterativo", "Bidirecional", "Custo Uniforme", "Greedy"]
dropdown = ttk.Combobox(frame_inputs, value=opcoes)
dropdown.grid(row=7, column=0, columnspan=2, pady=5)
dropdown.current(0)

# Botão
btn_Executar = tk.Button(frame_esquerda, text="Executar", command=lambda: print("Botão clicado"))
btn_Executar.pack(pady=20)

# ---- Área direita (Grid e Texto) ----
frame_grid = tk.Frame(frame_direita, bg="white", width=900, height=600)
frame_grid.pack(expand=True, fill="both", padx=20, pady=20)

# Criando um Canvas para desenhar a grid
canvas = tk.Canvas(frame_grid, bg="white")
canvas.pack(expand=True, fill="both")

# Parâmetros da grid
GRID_WIDTH = 20   # Largura
GRID_HEIGHT = 20  # Altura
CELL_SIZE = 30    # Tamanho de cada célula em pixels

# Calculando a posição centralizada dentro do canvas
canvas_width = GRID_WIDTH * CELL_SIZE
canvas_height = GRID_HEIGHT * CELL_SIZE

canvas.config(width=canvas_width, height=canvas_height)  # Define o tamanho fixo do canvas

def desenhar_grid():
    """Função para desenhar a grade no Canvas"""
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            x1, y1 = j * CELL_SIZE, i * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, outline="black")

desenhar_grid()

# Centralizando o canvas dentro do frame_grid
canvas.place(relx=0.5, rely=0.5, anchor="center")

# Campo de resultado
label_resultado = tk.Label(frame_direita, text="Resultado aparecerá aqui", fg="blue", font=("Arial", 12, "bold"))
label_resultado.pack(pady=10)

janela.mainloop()