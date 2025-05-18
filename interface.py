import tkinter as tk
from tkinter import ttk
from busca_sem_pesos import buscaGridNP

# Criar a janela principal
janela = tk.Tk()
janela.title("Busca em Grid")
janela.state('zoomed')

# Criando os frames principais
frame_esquerda = tk.Frame(janela, width=400)
frame_esquerda.pack(side="left", fill="y")
frame_esquerda.pack_propagate(False)

frame_legenda = None

frame_direita = tk.Frame(janela)
frame_direita.pack(side="right", expand=True, fill="both")

frame_limite = None
entry_limite = None

def on_metodo_selecionado(event):
    global frame_limite, entry_limite
    
    metodo = metodo_selecionado.get()
    
    # Remove o frame de limite se existir
    if frame_limite:
        frame_limite.destroy()
        frame_limite = None
        entry_limite = None
    
    # Cria novo frame de limite se necessário
    if metodo in ["Profundidade Limitada", "Aprofundamento Iterativo"]:
        frame_limite = tk.Frame(frame_inputs)
        frame_limite.grid(row=8, column=0, columnspan=2, pady=5, sticky="ew")
        
        label_text = "Limite:" if metodo == "Profundidade Limitada" else "Profundidade Máxima:"
        tk.Label(frame_limite, text=label_text).pack(side="left", padx=5)
        
        entry_limite = tk.Entry(frame_limite, width=10)
        entry_limite.pack(side="left")
        entry_limite.insert(0, "15")  # Valor padrão
        
        # Ajusta a posição do botão para baixo do novo frame
        btn_executar.grid(row=9, column=0, columnspan=2, pady=20)
    else:
        # Volta o botão para a posição original
        btn_executar.grid(row=8, column=0, columnspan=2, pady=20)
    
    # Limpa a grid e redesenha sem caminho quando o método é alterado
    matriz = carregar_matriz()
    if matriz and inicio_coord and objetivo_coord:
        desenhar_grid(matriz, inicio=inicio_coord, fim=objetivo_coord)
    elif matriz:
        desenhar_grid(matriz)

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
metodos = ["Amplitude", "Profundidade", "Profundidade Limitada", "Aprofundamento Iterativo", "Bidirecional", "Custo Uniforme", "Greedy", "A Estrela", "AIA Estrela"]
metodo_selecionado = tk.StringVar()
dropdown_metodo = ttk.Combobox(frame_inputs, textvariable=metodo_selecionado, values=metodos)
dropdown_metodo.grid(row=7, column=0, columnspan=2, pady=5)
dropdown_metodo.bind("<<ComboboxSelected>>", on_metodo_selecionado)

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

frame_resultado = tk.Frame(frame_direita)
frame_resultado.pack(fill="both", expand=False, pady=10)

scrollbar = tk.Scrollbar(frame_resultado)
scrollbar.pack(side="right", fill="y")

text_resultado = tk.Text(frame_resultado, height=5, wrap="word", yscrollcommand=scrollbar.set, font=("Arial", 10), padx=10, pady=5, state="disabled")
text_resultado.pack(fill="both", expand=True)
scrollbar.config(command=text_resultado.yview)

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

def mostrar_legenda(mostrar=True):
    global frame_legenda
    
    if frame_legenda:
        frame_legenda.destroy()
        frame_legenda = None
    
    if mostrar:
        frame_legenda = tk.Frame(frame_esquerda)
        frame_legenda.pack(pady=10, padx=10, fill="x")
        
        tk.Label(frame_legenda, text="Legenda de Cores:", font=("Arial", 10, "bold")).pack(anchor="w")
        
        # Cria os itens da legenda
        def criar_item_legenda(cor, texto):
            frame = tk.Frame(frame_legenda)
            frame.pack(fill="x", pady=2)
            tk.Label(frame, width=3, height=1, bg=cor).pack(side="left", padx=5)
            tk.Label(frame, text=texto, font=("Arial", 9)).pack(side="left")
        
        criar_item_legenda("yellow", "Ponto Inicial")
        criar_item_legenda("red", "Ponto Objetivo")
        criar_item_legenda("green", "Caminho Encontrado")
        criar_item_legenda("black", "Obstáculo")
        criar_item_legenda("white", "Caminho Livre")

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
        
        if (x, y) == objetivo:
            return True
        
        if (x, y) in visitados:
            continue
        
        visitados.add((x, y))
        
        # Use as mesmas direções que na função sucessores
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx_pos, ny_pos = x + dx, y + dy
            
            # Verifique da mesma forma que em sucessores()
            if 0 <= nx_pos < nx and 0 <= ny_pos < ny and matriz[ny_pos][nx_pos] != 9:
                fila.append((nx_pos, ny_pos))
    
    return False

# ---- Função para executar a busca ----
def executar_busca():
    mostrar_legenda(False)

    metodos_disponiveis = {
        "Amplitude": busca.amplitude,
        "Profundidade": busca.profundidade,
        "Profundidade Limitada": busca.prof_limitada,
        "Aprofundamento Iterativo": busca.aprof_iterativo,
        "Bidirecional": busca.bidirecional,
        "Custo Uniforme": busca.custo_uniforme,
        "Greedy": busca.greedy,
        "A Estrela": busca.a_estrela,
        "AIA Estrela": busca.aia_estrela
    }

    try:
        # Habilita temporariamente para edição
        text_resultado.config(state="normal")
        # Limpa o resultado anterior
        text_resultado.delete(1.0, tk.END)
        
        inicio_x = int(entry_InicioX.get())
        inicio_y = int(entry_InicioY.get())
        objetivo_x = int(entry_ObjetivoX.get())
        objetivo_y = int(entry_ObjetivoY.get())
        
        matriz = carregar_matriz()
        
        if not matriz:
            text_resultado.insert(tk.END, "Erro: Não foi possível carregar a matriz!", "error")
            text_resultado.config(state="disabled")
            return

        nx, ny = len(matriz[0]), len(matriz)  # Dimensões da matriz (x, y)

        # Verifica se as coordenadas estão dentro dos limites da matriz
        if not (0 <= inicio_x < nx and 0 <= inicio_y < ny):
            text_resultado.insert(tk.END, "Erro: Coordenada de início fora do grid!", "error")
            return
        
        if not (0 <= objetivo_x < nx and 0 <= objetivo_y < ny):
            text_resultado.insert(tk.END, "Erro: Coordenada de objetivo fora do grid!", "error")
            return

        # Verifica se o início ou o objetivo são obstáculos
        if matriz[inicio_y][inicio_x] == 9:
            text_resultado.insert(tk.END, "Erro: O ponto de início é um obstáculo!", "error")
            return

        if matriz[objetivo_y][objetivo_x] == 9:
            text_resultado.insert(tk.END, "Erro: O ponto de objetivo é um obstáculo!", "error")
            return
        
        # Verificar se existe pelo menos um caminho possível
        if not verificar_conexao((inicio_x, inicio_y), (objetivo_x, objetivo_y), nx, ny, matriz):
            text_resultado.insert(tk.END, "Erro: Não existe caminho possível entre início e objetivo!", "error")
            return

        metodo = metodo_selecionado.get()

        if metodo not in metodos_disponiveis:
            text_resultado.insert(tk.END, "Erro: Selecione um método válido", "error")
            return
        
        inicio = [inicio_x, inicio_y]
        objetivo = [objetivo_x, objetivo_y]

        # Chama a busca correspondente
        if metodo == "Profundidade Limitada":
            if not entry_limite:
                text_resultado.insert(tk.END, "Erro: Defina um limite para a busca!", "error")
                return
            try:
                limite = int(entry_limite.get())
                caminho = metodos_disponiveis[metodo](inicio, objetivo, nx, ny, matriz, limite)
            except ValueError:
                text_resultado.insert(tk.END, "Erro: O limite deve ser um número inteiro!", "error")
                return
        elif metodo == "Aprofundamento Iterativo":
            if not entry_limite:
                text_resultado.insert(tk.END, "Erro: Defina uma profundidade máxima!", "error")
                return
            try:
                profundidade_max = int(entry_limite.get())
                caminho = metodos_disponiveis[metodo](inicio, objetivo, nx, ny, matriz, profundidade_max)
            except ValueError:
                text_resultado.insert(tk.END, "Erro: A profundidade máxima deve ser um número inteiro!", "error")
                return
        elif metodo == "AIA Estrela":
            if not entry_limite:
                # Usa heurística como limite padrão se não for fornecido
                limite = None
            else:
                try:
                    limite = int(entry_limite.get())
                except ValueError:
                    text_resultado.insert(tk.END, "Erro: O limite deve ser um número inteiro!", "error")
                    return
            caminho = metodos_disponiveis[metodo](inicio, objetivo, nx, ny, matriz, limite)
        else:
            caminho = metodos_disponiveis[metodo](inicio, objetivo, nx, ny, matriz)

        if caminho:
            caminho = [(estado[0], estado[1]) for estado in caminho]
            desenhar_grid(matriz, caminho, inicio=(inicio_x, inicio_y), fim=(objetivo_x, objetivo_y))
        
            # Mostra informações resumidas e detalhadas com quebra de linha
            text_resultado.insert(tk.END, f"Caminho encontrado com {len(caminho)} passos:\n", "success")
        
            # Divide o caminho em linhas de 10 coordenadas cada
            for i in range(0, len(caminho), 15):
                parte = caminho[i:i+15]
                linha = " → ".join([f"({x},{y})" for x, y in parte])
                if i + 15 < len(caminho):
                    linha += " →\n"
                text_resultado.insert(tk.END, linha)
        
            # Mostra a legenda após encontrar um caminho
            mostrar_legenda(True)
        else:
            desenhar_grid(matriz, inicio=(inicio_x, inicio_y), fim=(objetivo_x, objetivo_y))
            text_resultado.insert(tk.END, "Nenhum caminho encontrado!", "error")
        
            # Mostra a legenda mesmo sem caminho encontrado
            mostrar_legenda(True)

    except ValueError:
        text_resultado.insert(tk.END, "Erro: Certifique-se de que todas as coordenadas são números inteiros.", "error")
    
    text_resultado.config(state="disabled")

# Adicione tags para formatação (coloque isso após criar o text_resultado)
text_resultado.tag_configure("success", foreground="green", font=("Arial", 10, "bold"))
text_resultado.tag_configure("error", foreground="red", font=("Arial", 10, "bold"))
text_resultado.tag_configure("header", font=("Arial", 10, "underline"))

# Botão para executar a busca
btn_executar = tk.Button(frame_inputs, text="Executar Busca", command=executar_busca)
btn_executar.grid(row=8, column=0, columnspan=2, pady=20)

# Carregar e desenhar a matriz ao iniciar
matriz_inicial = carregar_matriz()
desenhar_grid(matriz_inicial)

canvas.bind("<Button-1>", selecionar_ponto)
janela.mainloop()