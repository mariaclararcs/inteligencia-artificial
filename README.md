# 🔍 Busca de Rotas - Grid

### Cenário da atividade proposta

Este projeto tem como objetivo aplicar algoritmos de busca em grafos para encontrar rotas dentro de um grid. A interface gráfica permite que o usuário defina pontos de início e destino, além de visualizar o caminho encontrado pelo algoritmo escolhido.

### Métodos de Busca Implementados

🔹 **Amplitude (BFS - Breadth-First Search):**

Explora primeiro os nós mais próximos ao nó inicial, expandindo a busca em camadas. É garantido que encontra o caminho mais curto em grafos sem pesos.

🔹 **Profundidade (DFS - Depth-First Search):**

Explora um caminho até o fim antes de retroceder e explorar outras alternativas. Pode ser mais eficiente em alguns casos, mas não garante o menor caminho.

🔹 **Profundidade Limitada:**

Variante do DFS que limita a profundidade máxima da busca. Se o objetivo estiver além do limite, pode não ser encontrado.

🔹 **Aprofundamento Iterativo:**

Executa múltiplas buscas DFS com profundidade crescente até encontrar a solução. Combina características do BFS e DFS.

🔹 **Bidirecional:**

Realiza a busca simultaneamente a partir do início e do objetivo, reduzindo o espaço de busca necessário.

🔹 **Custo Uniforme:**

Encontra o caminho com menor custo total, considerando diferentes pesos para cada movimento. Garante a solução ótima para grafos com pesos não-negativos.

🔹 **Greedy (Melhor Primeiro):**

Utiliza uma função heurística para estimar a distância até o objetivo, sempre expandindo o nó mais promissor. Não garante o caminho ótimo, mas geralmente é rápido.

🔹 **A Estrela:**

Combina o custo real do caminho com uma estimativa heurística do custo restante. Garante encontrar o caminho de menor custo se a heurística for admissível (não superestimar).

🔹 **AIA Estrela:**

Versão iterativa do A* que ajusta progressivamente o limite de custo. Combina as vantagens do Aprofundamento Iterativo com o A*, sendo eficiente em memória.

---

## Como rodar o projeto

### Requisitos

- Versão do **Python**: 3.8 ou superior.
- Biblioteca **Tkinter** (padrão do Python).

💻 **Instalação do Python:**

Caso não tenha o Python instalado:
- Acesse o site oficial: (https://www.python.org/downloads/)
- Baixe a versão compatível com o sistema operacional.
- Durante a instalação, marque a opção **Add Python to PATH**.

▶️ **Como executar:**

Com o Python instalado, basta navegar até a pasta do projeto no terminal e rodar:
```
py interface.py
```
Isso iniciará uma janela, e você poderá acessar o projeto.

Para executar a busca:
- Insira coordenadas **Início** válidas nos campos (X e Y) ou clique em um ponto na grid.
- Insira coordenadas **Objetivo** válidas nos campos (X e Y) ou clique em um ponto na grid.
- Escolha um método de busca.
- Caso o método for **Profundidade Limitada**, insira um valor para limite.
- Caso o método for **Aprofundamento Iterativo**, insira um valor para profundidade máxima.
- Clique em **Executar Busca**.

O campo de início será mostrado em amarelo, o objetivo em vermelho e o caminho encontrado será mostrado em verde. Também será mostrada as coordenadas do caminho encontrado.
