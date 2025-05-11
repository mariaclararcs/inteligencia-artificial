from listaDEnc import listaDEnc

class buscaGridNP(object):
    
    # SUCESSORES PARA GRID (LISTA DE ADJACENCIAS)
    def sucessores(self, st, nx, ny, mapa):
        f = []
        x = st[0]
        y = st[1]
    
        # Verifique se as coordenadas estão dentro dos limites
        if x < 0 or x >= nx or y < 0 or y >= ny:
            return f
    
        # Direções possíveis (4 ou 8 conexões)
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1,-1), (-1,1), (1,-1), (1,1)]  # Apenas movimentos ortogonais
        # Para movimentos diagonais, adicione: (-1,-1), (-1,1), (1,-1), (1,1)
    
        for dx, dy in direcoes:
            nx_pos = x + dx
            ny_pos = y + dy
        
            # Verifique limites e obstáculos
            if 0 <= nx_pos < nx and 0 <= ny_pos < ny:
                # Verifique se é caminho livre (0) e não obstáculo (9)
                if mapa[ny_pos][nx_pos] == 0:  # Note a inversão de ny_pos/nx_pos aqui
                    suc = [nx_pos, ny_pos]
                    f.append(suc)
    
        return f
#------------------------------------------------------------------------------    
    # CONTROLE DE NÓS REPETIDOS
    def verificaVisitado(self,novo,nivel,visitado):
        flag = True
        # controle de nós repetidos
        for aux in visitado:
            if aux[0]==novo:
                if aux[1]<=(nivel+1):
                    flag = False
                else:
                    aux[1]=nivel+1
                break
        return flag
#------------------------------------------------------------------------------
    # BUSCA EM AMPLITUDE
    def amplitude(self,inicio,fim,nx,ny,mapa):

        # manipular a FILA para a busca
        l1 = listaDEnc()

        # cópia para apresentar o caminho (somente inserção)
        l2 = listaDEnc()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()
            
            filhos = self.sucessores(atual.estado,nx,ny,mapa)

            # varre todos as conexões dentro do grafo a partir de atual
            for novo in filhos:

                # verifica se foi visitado
                flag = self.verificaVisitado(novo,atual.v1,visitado)

                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo,atual.v1+1,0,atual)
                    l2.insereUltimo(novo,atual.v1+1,0,atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.v1+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        #print("\nFila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return None
#------------------------------------------------------------------------------
    # BUSCA EM PROFUNDIDADE
    def profundidade(self,inicio,fim,nx,ny,mapa):
        # manipular a PILHA para a busca
        l1 = listaDEnc()

        # cópia para apresentar o caminho (somente inserção)
        l2 = listaDEnc()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o último da PILHA
            atual = l1.deletaUltimo()
            
            filhos = self.sucessores(atual.estado,nx,ny,mapa)

            # varre todos as conexões dentro do grafo a partir de atual
            for novo in filhos:

                # verifica se foi visitado
                flag = self.verificaVisitado(novo,atual.v1,visitado)

                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo,atual.v1+1,0,atual)
                    l2.insereUltimo(novo,atual.v1+1,0,atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.v1+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        #print("\nFila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return None
#------------------------------------------------------------------------------
    # BUSCA EM PROFUNDIDADE LIMITADA
    def prof_limitada(self,inicio,fim,nx,ny,mapa,lim):
        # manipular a PILHA para a busca
        l1 = listaDEnc()

        # cópia para apresentar o caminho (somente inserção)
        l2 = listaDEnc()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o último da PILHA
            atual = l1.deletaUltimo()
            if atual.v1<lim:
                filhos = self.sucessores(atual.estado,nx,ny,mapa)
    
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:
    
                    # verifica se foi visitado
                    flag = self.verificaVisitado(novo,atual.v1,visitado)
    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo,atual.v1+1,0,atual)
                        l2.insereUltimo(novo,atual.v1+1,0,atual)
    
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.v1+1)
                        visitado.append(linha)
    
                        # verifica se é o objetivo
                        if novo == fim:
                            caminho = []
                            caminho += l2.exibeCaminho()
                            #print("\nFila:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            return caminho

        return None    
    # BUSCA EM APROFUDAMENTO ITERATIVO
    def aprof_iterativo(self,inicio,fim,nx,ny,mapa,l_max):
        for lim in range(1,l_max):
            # manipular a PILHA para a busca
            l1 = listaDEnc()
    
            # cópia para apresentar o caminho (somente inserção)
            l2 = listaDEnc()
    
            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio,0,0,None)
            l2.insereUltimo(inicio,0,0,None)
    
            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
    
            while l1.vazio() == False:
                # remove o último da PILHA
                atual = l1.deletaUltimo()
                if atual.v1<lim:
                    filhos = self.sucessores(atual.estado,nx,ny,mapa)
        
                    # varre todos as conexões dentro do grafo a partir de atual
                    for novo in filhos:
        
                        # verifica se foi visitado
                        flag = self.verificaVisitado(novo,atual.v1,visitado)
        
                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo,atual.v1+1,0,atual)
                            l2.insereUltimo(novo,atual.v1+1,0,atual)
        
                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.v1+1)
                            visitado.append(linha)
        
                            # verifica se é o objetivo
                            if novo == fim:
                                caminho = []
                                caminho += l2.exibeCaminho()
                                #print("\nFila:\n",l1.exibeLista())
                                #print("\nÁrvore de busca:\n",l2.exibeLista())
                                return caminho

        return None    
#------------------------------------------------------------------------------
    # BUSCA BIDIRECIONAL
    def bidirecional(self,inicio,fim,nx,ny,mapa):
        # Primeiro Amplitude"
        # Manipular a FILA para a busca
        l1 = listaDEnc()
        # cópia para apresentar o caminho (somente inserção)
        l2 = listaDEnc()
        
        # Segundo Amplitude"
        # Manipular a FILA para a busca
        l3 = listaDEnc()
        # cópia para apresentar o caminho (somente inserção)
        l4 = listaDEnc()
    
        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        
        l3.insereUltimo(fim,0,0,None)
        l4.insereUltimo(fim,0,0,None)
        
        # controle de nós visitados
        visitado1 = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado1.append(linha)
        
        visitado2 = []
        linha = []
        linha.append(fim)
        linha.append(0)
        visitado2.append(linha)
        
        ni = 0
        while l1.vazio()==False or l3.vazio()==False:
            
            while l1.vazio() == False:
                
                # para ir para o próximo amplitude
                if ni!=l1.primeiro().v1:
                    break
                    
                # remove o primeiro da fila
                atual = l1.deletaPrimeiro()
        
                filhos = self.sucessores(atual.estado,nx,ny,mapa)
        
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:
        
                    # pressuponho que não foi visitado
                    flag = self.verificaVisitado(novo,atual.v1+1,visitado1)
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo,atual.v1+1,0,atual)
                        l2.insereUltimo(novo,atual.v1+1,0,atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.v1+1)
                        visitado1.append(linha)
        
                        # verifica se é o objetivo
                        flag = not(self.verificaVisitado(novo,atual.v1+1,visitado2))
                        if flag:
                            caminho = []
                            #print("Fila:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            caminho += l2.exibeCaminho()
                            caminho += l4.exibeCaminho1(novo)
                            return caminho
                        
            while l3.vazio() == False:
                
                # para ir para o próximo amplitude
                if ni!= l3.primeiro().v1:
                    break
                
                # remove o primeiro da fila
                atual = l3.deletaPrimeiro()
        
                filhos = self.sucessores(atual.estado,nx,ny,mapa)
        
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:
        
                    # pressuponho que não foi visitado
                    flag = self.verificaVisitado(novo,atual.v1+1,visitado2)
                    # se não foi visitado inclui na fila
                    if flag:
                        l3.insereUltimo(novo,atual.v1+1,0,atual)
                        l4.insereUltimo(novo,atual.v1+1,0,atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.v1+1)
                        visitado2.append(linha)
        
                        # verifica se é o objetivo
                        flag = not(self.verificaVisitado(novo,atual.v1+1,visitado1))
                        if flag:
                            caminho = []
                            #print("Fila:\n",l3.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            caminho += l4.exibeCaminho()
                            caminho += l2.exibeCaminho1(novo)
                            return caminho[::-1]
                            
            ni += 1
    
        return "caminho não encontrado"