import logging
from pprint import pprint

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
    print("Matriz de adjacencia: ")
    pprint(matAdjacencia)
    nrLimitados = int(input())
    print("Numero de Limitados: "+str(nrLimitados))
    listaLimitados = input().split(' ')
    print("Limitados: "+str(listaLimitados))

#----------------------------------------
#Funções:
#----------------------------------------

