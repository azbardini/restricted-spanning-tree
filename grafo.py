from numpy import * 

#----------------------------------------
#Classe grafo com algorritmo padrão de PRIM:
#----------------------------------------

class Grafo(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.grafo = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    #soma e retorna
    def getMSTSum(self, predecessor): 
        #print ("Edge \tWeight")
        total = 0
        for i in range(1,self.V): 
            total += self.grafo[i][predecessor[i]]
        return total

    #função que encontra o vertice de menor dinstancia, se ainda não
    #incluido na arvore de caminhos minimos
    def menorChave(self, chave, listaIncluidos): 
        min = 100000 
        for v in range(self.V): 
            if chave[v] < min and listaIncluidos[v] == False: 
                min = chave[v] 
                min_index = v 
        return min_index 
  
    # função que constroi e retorna a MST de um grafo em matriz de adjacencia 
    def primMST(self): 
        
        #custo infinito nos vertices 
        chave = [100000] * self.V 
        
        #anterior setado como ninguém
        predecessor = [None] * self.V 
        
        #usa o vertice 0 de inicial
        chave[0] = 0

        #esvazia lista de já verificados
        listaIncluidos = [False] * self.V

        #seta a raiz com -1 no anterior
        predecessor[0] = -1 

        for contador in range(self.V): 
  
            #pega a menor chave dentro dos vertices não percorridos
            u = self.menorChave(chave, listaIncluidos) 
            
            #coloca o vertice de menor distancia na arvore de menores caminhos  
            listaIncluidos[u] = True
  
            #atualiza a distancia dos vertices adjascentes ao escolhido,
            #se a distancia atual é maior que a nova distancia e 
            #o vertice não esta na arvore de menores caminhos  
            for v in range(self.V): 

                # grafo[u][v] só é 0 em caso de não adjacencia 
                # listaIncluidos[v] é falso pra vertices que não estão ainda na MST 
                # só atualiza a chave se grafo[u][v] é menor que chave[v] 
                if self.grafo[u][v] > 0 and listaIncluidos[v] == False and chave[v] > self.grafo[u][v]: 
                        chave[v] = self.grafo[u][v] 
                        predecessor[v] = u 
        
        return self.getMSTSum(predecessor)

def main():

    #----------------------------------------
    #Importando Dados:
    #----------------------------------------
    nrCampi = int(input())
    #print("Numero de Campi: "+str(nrCampi))
    for campi in range(0, nrCampi):
        #print("\nCampi "+str(campi))
        nrDispositivo = int(input())
        #print("Numero de Dispositivos: "+str(nrDispositivo))
        matAdjacencia = []
        for dispositivo in range(0, nrDispositivo):
            matAdjacencia.append(input().split(' '))
        for i in range(0,nrDispositivo):
            for j in range(0,nrDispositivo):
                matAdjacencia[i][j] = int(matAdjacencia[i][j])
        #print("Matriz de adjacencia: ")
        #print(matAdjacencia)

        nrLimitados = int(input())
        #print("Numero de Limitados: "+str(nrLimitados))
        listaLimitados = input().split(' ')
        for i in range(0,nrLimitados):
            listaLimitados[i] = int(listaLimitados[i])
        #print("Limitados: "+str(listaLimitados))
        soma = 0
        for limitado in listaLimitados:
            menor = 100000 
            for i, vert in enumerate(matAdjacencia[limitado-1]):
                if vert < menor and limitado != i+1 and i+1 not in listaLimitados:
                    menor = vert
            soma += menor
        listaLimitados.sort()
        for limitado in reversed(listaLimitados):
            matAdjacencia = delete(matAdjacencia, [limitado-1],0)
            matAdjacencia = delete(matAdjacencia, [limitado-1],1)
            nrDispositivo = nrDispositivo-1

        #print("Matriz de adjacencia removida: ")
        #print(matAdjacencia)
#----------------------------------------
#Chamando PRIM
#----------------------------------------
        #print("\nPrim Tree: ")
        g1 = Grafo(nrDispositivo)
        g1.grafo = matAdjacencia
        prim = g1.primMST()
        print("Campus " + str(campi+1) + ': ' + str(soma + prim))

if __name__ == "__main__":
    main()