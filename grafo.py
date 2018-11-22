import logging
from pprint import pprint
from numpy import * 

#----------------------------------------
#Funções:
#----------------------------------------

class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    # Printador
    def printMST(self, parent): 
        print ("Edge \tWeight")
        total = 0
        for i in range(1,self.V): 
            total += self.graph[i][parent[i]]
            print (parent[i],"-",i,"\t",self.graph[i][parent[i]])
        print ("Total: "+str(total))
        return total

    #função que encontra o vertice de menor dinstancia, se ainda não
    #incluido na arvore de caminhos minimos
    def minKey(self, key, mstSet): 
        min = 100000 
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
        return min_index 
  
    # Function to construct and print MST for a graph  
    # represented using adjacency matrix representation 
    def primMST(self): 
        #custo infinito nos vertices 
        key = [100000] * self.V 
        #anterior setato como ninguém
        parent = [None] * self.V # Array to store constructed MST 
        #Usa o vertice 0 de inicial
        key[0] = 0 
        #esvazia lista de já verificados
        mstSet = [False] * self.V
        #seta a raiz com -1 no anterior
        parent[0] = -1 # First node is always the root of 
  
        for cout in range(self.V): 
  
            #pega a menor chave dentro dos vertices não percorridos
            # u is always equal to src in first iteration 
            u = self.minKey(key, mstSet) 
            # coloca o vertice de menor distancia na arvore de menores caminhos  
            mstSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            #atualiza a distancia dos vertices adjascentes ao escolhido,
            #somente se a distancia atual é maior que a nova distancia e 
            #o vertice não esta na arvore de menores caminhos  
            for v in range(self.V): 
                # graph[u][v] is non zero only for adjacent vertices of m 
                # mstSet[v] is false for vertices not yet included in MST 
                # Update the key only if graph[u][v] is smaller than key[v] 
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
        
        self.printMST(parent)


#----------------------------------------
#Importando Dados:
#----------------------------------------
nrCampi = int(input())
pprint("Numero de Campi: "+str(nrCampi))
for campi in range(0, nrCampi):
    print("\nCampi "+str(campi))
    nrDispositivo = int(input())
    print("Numero de Dispositivos: "+str(nrDispositivo))
    matAdjacencia = []
    for dispositivo in range(0, nrDispositivo):
        matAdjacencia.append(input().split(' '))
    for i in range(0,nrDispositivo):
        for j in range(0,nrDispositivo):
            matAdjacencia[i][j] = int(matAdjacencia[i][j])
    print("Matriz de adjacencia: ")
    for ins in matAdjacencia:
        print (ins)

    nrLimitados = int(input())
    print("Numero de Limitados: "+str(nrLimitados))
    listaLimitados = input().split(' ')
    for i in range(0,nrLimitados):
        listaLimitados[i] = int(listaLimitados[i])
    print("Limitados: "+str(listaLimitados))
    soma = 0
    for limitado in listaLimitados:
        menor = 100000 
        for i, vert in enumerate(matAdjacencia[limitado-1]):
            if vert < menor and vert > 0 and i+1 not in listaLimitados:
                menor = vert
        soma += menor
    for limitado in reversed(listaLimitados):
        matAdjacencia = delete(matAdjacencia, [limitado-1],0)
        matAdjacencia = delete(matAdjacencia, [limitado-1],1)
        nrDispositivo = nrDispositivo-1
        
    print("Matriz de adjacencia removidaaaaa: ")
    for ins in matAdjacencia:
        print (ins)


#----------------------------------------
#Chamando PRIM
#----------------------------------------
    print("\nPrim Tree: ")
    grafo = Graph(nrDispositivo)
    grafo.graph = matAdjacencia
    prim = grafo.primMST()
    print("Soma: "+ str(soma))
    print("Campi " + str(campi+1) + ' '+ str(prim))