#************************ATENÇÃO*************************#
#Esse algoritmo deve ser executado utilizando-se Python 3#
#********************************************************#

#O algoritmo retorna o custo em arestas para 
#o caminhamento em um grafo utilizando uma variante
#do algoritmo de prim.
#Em adição, são colocados os vertices que só poderiam 
#ter uma conexão.
#Dessa forma, o algoritmo retorna a quantidade minima de cabos
#necessários no problema da reforma da universidade descrito 
#no trabalho.

class Grafo(): 

    def __init__(self, vertices): 
        self.V = vertices 
       
    #função que encontra o vertice de menor distancia, se ainda não
    #incluido na arvore de caminhos minimos
    def menorChave(self, chave, listaIncluidos): 
        min = 100000 
        for v in range(self.V): 
            if chave[v] < min and listaIncluidos[v] == False: 
                min = chave[v] 
                menorIndice = v 
        return menorIndice 
  
    # função que constroi e retorna a MST de um grafo em matriz de adjacencia 
    def prim(self): 
        
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
  
            #atualiza a distancia dos vertices adjascentes ao escolhido
            for v in range(self.V): 
                if self.grafo[u][v] > 0 and listaIncluidos[v] == False and chave[v] > self.grafo[u][v]: 
                        chave[v] = self.grafo[u][v] 
                        predecessor[v] = u 

        #retorna a soma de todos os predecessores 
        #da matriz de adjacencia
        total = 0
        for i in range(1,self.V): 
            total += self.grafo[i][predecessor[i]]
        return total

def main():

    #----------------------------------------
    #Importando Dados:
    #----------------------------------------
    nrCampi = int(input())
    #Para cada campi do arquivo, faz as seguintes operações:
    for campi in range(0, nrCampi):

        #Encontra o número de dispositivos
        nrDispositivo = int(input())

        #Preenche a matriz de adjacencia dos cabos (arestas)
        matAdjacencia = []
        for dispositivo in range(0, nrDispositivo):
            matAdjacencia.append(input().split(' '))

        #Transforma a matriz em numeros inteiros
        for i in range(0,nrDispositivo):
            for j in range(0,nrDispositivo):
                matAdjacencia[i][j] = int(matAdjacencia[i][j])
        nrLimitados = int(input())

        #Encontra a quantidade de dispositivos limitados a uma única conexão
        listaLimitados = input().split(' ')

        #Transforma a lista deles em numeros inteiros
        for i in range(0,nrLimitados):
            listaLimitados[i] = int(listaLimitados[i])

        #Acumula o menor vertice de cada dispositivo limitado 
        soma = 0
        for limitado in listaLimitados:
            menor = 100000 
            for i, vert in enumerate(matAdjacencia[limitado-1]):
                if vert < menor and limitado != i+1 and i+1 not in listaLimitados:
                    menor = vert
            soma += menor

        #Remove da lista de adjacencia as linahs e colunas correspondentes 
        #aos vertices limitados 
        listaLimitados.sort()
        for limitado in reversed(listaLimitados):
            #matAdjacencia = delete(matAdjacencia, [limitado-1],0)
            #matAdjacencia = delete(matAdjacencia, [limitado-1],1)
            #estruturas acima utilizam NUMPY, foi substituido por
            #loops abaixo para só utilizar bibliotecas padrão.
            matAdjacencia.pop(limitado-1)
            for inst in matAdjacencia:
                inst.pop(limitado-1)
            nrDispositivo = nrDispositivo-1

        #Cria a instancia de Grafo
        g1 = Grafo(nrDispositivo)

        #Seta o grafo como a matriz de adjacencia
        g1.grafo = matAdjacencia

        #Chama a arvore PRIM para a lista de adjacencias
        prim = g1.prim()

        #Printa a soma resultante da PRIM com a resultante dos vertices limitados
        print("Campus " + str(campi+1) + ': ' + str(soma + prim))

if __name__ == "__main__":
    main()